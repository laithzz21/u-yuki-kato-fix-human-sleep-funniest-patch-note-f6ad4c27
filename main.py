#!/usr/bin/env python3
"""make.fun entry: fix human sleep — funniest patch note.

Prints a single-line patch note (under 160 characters) announcing
that human sleep has been fixed. Deterministic, standard library
only, no network, clock, or randomness.
"""

import os

ENTRY = (
    "Fixed: humans now fall asleep in under 10 minutes. "
    "Waking up tired is deprecated and will be removed in a future update."
)

MAX_LENGTH = 160


def validate_entry(text):
    """Ensure the patch note is a single line under the 160-char limit."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be empty")
    if len(text) >= MAX_LENGTH:
        raise ValueError("entry must be under 160 characters")
    return text


def get_entry():
    """Return the validated patch note, falling back to a safe short form."""
    try:
        return validate_entry(ENTRY)
    except ValueError:
        return "Fixed: human sleep now works. Waking up tired is deprecated."


def main():
    entry = get_entry()
    print(entry)
    output_path = os.environ.get("MAKEFUN_OUTPUT")
    if output_path:
        with open(output_path, "w", encoding="utf-8") as handle:
            handle.write(entry + "\n")


if __name__ == "__main__":
    main()
