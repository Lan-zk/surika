"""Local Surika Markdown records. Python 3.9+, standard library only."""
import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import uuid


def record_path(folder, key):
    if not re.fullmatch(r"[\w-][\w.-]*", key):
        raise ValueError("Use a record ID from search (without .md).")
    path = folder / (key + ".md")
    if path.is_symlink():
        raise ValueError("Cannot modify or follow a symbolic record.")
    return path


def revision(data):
    return hashlib.sha256(data).hexdigest()


def summary(body):
    return next((line.strip().lstrip("#").strip() for line in body.splitlines()
                 if line.strip()), "")


def references(body):
    # Managed relationships use a local Markdown link to another record.
    return set(re.findall(r"\]\(\./([\w-][\w.-]*)\.md\)", body))


@contextmanager
def writer_lock(folder):
    # OS releases the advisory lock if an agent exits during a write.
    folder.mkdir(parents=True, exist_ok=True, mode=0o700)
    with (folder / ".write-lock").open("a+b") as lock:
        if os.name == "nt":
            import msvcrt
            lock.seek(0)
            msvcrt.locking(lock.fileno(), msvcrt.LK_LOCK, 1)
        else:
            import fcntl
            fcntl.flock(lock, fcntl.LOCK_EX)
        yield


def search(folder, args):
    terms = [word.casefold() for word in args.terms]
    hits = []
    for path in folder.glob("*.md"):
        if path.is_symlink() or not path.is_file():
            continue
        body = path.read_text(encoding="utf-8")
        heading = summary(body)
        if args.ref and args.ref not in references(body):
            continue
        haystack = (path.stem + " " + body).casefold()
        if all(term in haystack for term in terms):
            rank = sum(term in heading.casefold() for term in terms)
            hits.append((-rank, path.stem, heading))
    hits.sort()
    return {"total": len(hits), "records": [
        {"id": key, "summary": heading}
        for _, key, heading in hits[args.offset:args.offset + args.limit]]}


def run(args):
    folder = args.root.expanduser() / "records"
    if args.command == "search":
        return search(folder, args)
    key = args.id if args.command != "add" else uuid.uuid4().hex
    path = record_path(folder, key)
    if args.command == "show":
        data = path.read_bytes()
        return {"id": key, "revision": revision(data), "body": data.decode("utf-8")}

    body = None
    if args.command in ("add", "update"):
        body = sys.stdin.read() if args.file is None else args.file.read_text(encoding="utf-8")
        if not body.startswith("# ") or not body.splitlines()[0][2:].strip():
            raise ValueError("Start the record with '# ' and a standalone summary.")

    if args.command != "add" and not path.is_file():
        raise ValueError("Record does not exist.")
    with writer_lock(folder):
        if args.command == "add" and path.exists():
            raise ValueError("ID collision. Retry.")
        if args.command != "add" and revision(path.read_bytes()) != args.revision:
            raise ValueError("Record changed. Read it again before editing.")
        if args.command == "delete":
            for other in folder.glob("*.md"):
                if other != path and other.is_file() and not other.is_symlink():
                    if key in references(other.read_text(encoding="utf-8")):
                        raise ValueError("Review incoming link in " + other.stem + " before deleting.")
            path.unlink()
            return {"deleted": key}
        for target in references(body):
            if not record_path(folder, target).is_file():
                raise ValueError("Missing relationship target: " + target)
        with tempfile.NamedTemporaryFile(dir=folder, delete=False) as tmp:
            pending = Path(tmp.name)
        try:
            data = body.encode("utf-8")
            pending.write_bytes(data)
            os.replace(pending, path)
        finally:
            pending.unlink(missing_ok=True)
        return {"id": key, "revision": revision(data), "path": str(path)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.home() / ".surika")
    commands = parser.add_subparsers(dest="command", required=True)
    find = commands.add_parser("search", help="Find all terms; return summaries only")
    find.add_argument("terms", nargs="*")
    find.add_argument("--ref", help="Find incoming record links")
    find.add_argument("--limit", type=int, default=8)
    find.add_argument("--offset", type=int, default=0)
    commands.add_parser("show").add_argument("id")
    for name in ("add", "update", "delete"):
        command = commands.add_parser(name)
        if name != "add":
            command.add_argument("id")
            command.add_argument("revision", help="Revision returned by show")
        if name != "delete":
            command.add_argument("--file", type=Path, help="Markdown input; defaults to stdin")
    args = parser.parse_args()
    if args.command == "search" and (args.limit < 1 or args.offset < 0):
        parser.error("limit must be positive and offset nonnegative")
    try:
        print(json.dumps(run(args), ensure_ascii=False))
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
