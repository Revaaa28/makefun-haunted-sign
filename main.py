"""Funniest Sign on a Haunted Server Room Door.

Writes one funny sign (79 characters) to /output/entry.txt.

The sign: a door notice for a haunted server room, where the ghost
outranks the living staff -- it has root access, and you do not.
"""

import os

ENTRY = "AUTHORIZED PERSONNEL AND ONE GHOST ONLY. The ghost has root access. You do not."

# The sealed gate accepts UTF-8 text of 1 to 120 characters, not only
# whitespace. Enforce the same bound here so a bad edit fails loudly
# instead of shipping an invalid entry.
assert ENTRY == ENTRY.strip() and 1 <= len(ENTRY) <= 120, "entry violates the gate"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
