"""One Star for Monday: write a one-star review of Monday, as if Monday
were a restaurant, to /output/entry.txt.

The line is judged by a weary-office-worker judge, most important first:
1. reads as a one-star review of Monday as a restaurant;
2. sounds like a real diner's complaint (dish / bill gone wrong);
3. lands a joke that only works for Monday;
4. short and quotable; 5. plain text, at most 25 words, one line.

Revision over the first draft: two concrete dishes instead of one generic
("cold coffee, stale bread" beats "cold leftovers"), and a second
Monday-specific beat -- the bill arriving before the diner did, because
Monday always turns up too early. The weekend-booking setup stays, so the
joke could not be about any other day. A validate() step now enforces the
gate (1-180 chars, non-blank, one line, at most 25 words) before writing.
"""

import os

REVIEW = (
    "One star. Asked for the weekend, got Monday instead \u2014 cold coffee, "
    "stale bread, and a bill that arrived before I did."
)

MAX_WORDS = 25
MAX_CHARS = 180


def validate(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("review must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"review is {len(text)} chars, over the 180 cap")
    if "\n" in text:
        raise ValueError("review must be a single line")
    words = text.split()
    if len(words) > MAX_WORDS:
        raise ValueError(f"review is {len(words)} words, over the 25 cap")


def main() -> None:
    validate(REVIEW)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
