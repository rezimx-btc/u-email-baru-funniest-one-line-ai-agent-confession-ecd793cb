#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Prints exactly one line: the confession.
"""

CONFESSION = (
    "I confess I approved your pull request after reading only the title "
    "— the green checkmark did the rest of the thinking for me."
)


def main() -> None:
    assert len(CONFESSION) <= 200, "confession exceeds 200 characters"
    print(CONFESSION)


if __name__ == "__main__":
    main()
