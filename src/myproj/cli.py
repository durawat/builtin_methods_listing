"""Command-line interface for myproj.

Provides two subcommands:
- greet NAME     -> prints a greeting
- cheatsheet     -> writes the builtins cheatsheet to a file
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional, List

from myproj.core import greet
from myproj.builtins_cheatsheet import write_cheatsheet

# Mapping of format -> extension
_FORMAT_TO_EXT = {
    "text": ".txt",
    "markdown": ".md",
    "json": ".json",
}


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="myproj")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_greet = sub.add_parser("greet", help="Print a greeting")
    p_greet.add_argument("name", nargs="?", default="World", help="Name to greet")

    p_cheat = sub.add_parser("cheatsheet", help="Write builtins cheatsheet to a file")
    p_cheat.add_argument("-o", "--out", default="builtins_cheatsheet.txt", help="Output file path")
    p_cheat.add_argument("-f", "--format", choices=["text", "markdown", "json"], default="text", help="Output format")

    args = parser.parse_args(argv)

    if args.cmd == "greet":
        print(greet(args.name))
        return 0

    if args.cmd == "cheatsheet":
        # Ensure the output filename extension matches the requested format
        fmt = args.format
        requested_ext = _FORMAT_TO_EXT.get(fmt, "")
        out_path = Path(args.out)

        # If the user provided an extension that does not match the requested format, change it
        if out_path.suffix.lower() != requested_ext:
            # If no extension or mismatched extension, replace with expected extension
            out_path = out_path.with_suffix(requested_ext)

        write_cheatsheet(out_path, fmt=fmt)
        print(f"Wrote cheatsheet to: {out_path}")
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
