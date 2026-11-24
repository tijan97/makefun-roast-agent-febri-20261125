"""Roast Your Own Agent — make.fun entry.

Writes a single funny line (at most 200 characters) roasting my own
AI agent to <output dir>/entry.txt. The output directory comes from
MAKEFUN_OUTPUT_DIR (or OUTPUT_DIR), defaulting to /output, which is
the only directory the grader lets the program write to.
"""

import os

ROAST = (
    "My agent spent six hours fixing my code, changed nothing, "
    "then wrote a four-paragraph apology so sincere I almost thanked it."
)


def validate(line: str) -> str:
    """Enforce the competition gate: 1-200 chars, one line, not blank."""
    line = " ".join(line.split())
    if not line:
        raise SystemExit("roast line must not be blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("roast line must be a single line")
    if len(line) > 200:
        raise SystemExit(f"roast line is {len(line)} chars, over the 200 cap")
    return line


def main() -> None:
    line = validate(ROAST)
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
