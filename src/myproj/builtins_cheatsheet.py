"""Builtins cheatsheet - function documentation and reference.

This module provides utilities to list, group and format Python's
builtins and a helper to write a nicely formatted cheatsheet to a file.
"""

import builtins
from collections import defaultdict
from pathlib import Path
from typing import Iterable, List, Optional, Union


def get_builtins_list() -> list:
    """
    Get all builtins functions and constants.
    
    Returns:
        A list of all builtin names (excluding private/magic items).
    """
    return sorted([name for name in dir(builtins) if not name.startswith('_')])


def group_builtins_by_initial() -> dict:
    """
    Group builtins by their initial alphabet letter.
    
    Returns:
        A dictionary with letters as keys and lists of names as values.
    """
    builtins_list = get_builtins_list()
    grouped = defaultdict(list)

    for name in builtins_list:
        initial = name[0].upper()
        grouped[initial].append(name)

    return dict(sorted(grouped.items()))


def format_builtins_cheatsheet() -> str:
    """
    Format builtins as a 4-column cheatsheet grouped by initial letter.
    
    Returns:
        A formatted string with the cheatsheet layout.
    """
    grouped = group_builtins_by_initial()
    lines: List[str] = []

    for letter, names in grouped.items():
        lines.append("""
{}""".format('=' * 80))
        lines.append(letter)
        lines.append("""{}""".format('=' * 80))

        # Format in 4 columns with a stable column width
        col_width = 20
        for i in range(0, len(names), 4):
            row = names[i:i + 4]
            formatted_row = "  ".join(name.ljust(col_width) for name in row)
            lines.append(formatted_row)

    return "\n".join(lines)


def format_builtins_cheatsheet_markdown() -> str:
    """Return a markdown-formatted cheatsheet.

    Each initial letter becomes a second-level header and the values are
    shown in a fixed-width code block laid out in columns.
    """
    grouped = group_builtins_by_initial()
    lines: List[str] = []

    for letter, names in grouped.items():
        lines.append(f"## {letter}")
        lines.append("```text")
        col_width = 20
        for i in range(0, len(names), 4):
            row = names[i:i + 4]
            lines.append("  ".join(name.ljust(col_width) for name in row))
        lines.append("```")

    return "\n".join(lines)


def write_cheatsheet(path: Union[Path, str], names: Optional[Iterable[str]] = None, *, include_total: bool = True, fmt: str = "text") -> Path:



    """Write the formatted builtins cheatsheet to `path`.

    Args:
        path: Where to write the cheatsheet (file path or Path).
        names: Optional iterable of builtin names to use (for testing).
        include_total: Whether to append a total count line.

    Returns:
        The Path to the written file.
    """
    path = Path(path)
    # Ensure parent exists
    if path.parent and not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

    if names is not None:
        # Provide an alternate grouping when names provided (tests)
        # Temporarily monkey with get_builtins_list by formatting here.
        original = get_builtins_list()
        try:
            # we won't change the global functions; just build a formatted string
            grouped = defaultdict(list)
            for n in sorted(names):
                if not n.startswith('_'):
                    grouped[n[0].upper()].append(n)

            # Build content similar to format_builtins_cheatsheet
            lines: List[str] = []
            for letter, vals in sorted(grouped.items()):
                lines.append('=' * 80)
                lines.append(letter)
                lines.append('=' * 80)
                col_width = 20
                for i in range(0, len(vals), 4):
                    row = vals[i:i + 4]
                    lines.append("  ".join(name.ljust(col_width) for name in row))

            if include_total:
                lines.append(f"\nTotal builtins: {len([n for n in names if not n.startswith('_')])}")

            content = "\n".join(lines)
        finally:
            _ = original  # no-op, keep original variable for clarity
    else:
        if fmt == "markdown":
            content = format_builtins_cheatsheet_markdown()
            if include_total:
                content = content + f"\n\nTotal builtins: {get_builtins_count()}"
        elif fmt == "json":
            # simple json list of names grouped by initial
            import json

            grouped = group_builtins_by_initial()
            content = json.dumps(grouped, indent=2)
        else:
            content = format_builtins_cheatsheet()
            if include_total:
                content = content + f"\n\nTotal builtins: {get_builtins_count()}"

    path.write_text(content, encoding="utf-8")
    return path


def get_builtins_count():
    """
    Get the total count of builtins.
    
    Returns:
        The number of builtin names.
    """
    return len(get_builtins_list())


if __name__ == "__main__":
    # When run as a script, write output to a file instead of spamming the terminal
    out = write_cheatsheet(Path.cwd() / "builtins_cheatsheet.txt")
    print(f"Wrote builtins cheatsheet to: {out}\nTotal builtins: {get_builtins_count()}")
