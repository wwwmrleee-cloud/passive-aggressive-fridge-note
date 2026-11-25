"""Notes From a Passive-Aggressive Fridge.

Writes one funny passive-aggressive note that a smart fridge leaves
for its owner to /output/entry.txt, exactly as the judge will read it:
a single line, dry, petty and specific.

The note (122 characters, one line):

    You put the leftovers in on Friday and called it 'meal prep.'
    I have been staring at them ever since. They have names now.

Why this one: it is the fridge's voice all the way through (inventory
smugness, not generic nagging), it names a concrete domestic habit
(Friday leftovers rebranded as "meal prep"), and the sting lands in the
last third -- the leftovers have been sitting there so long they have
names now. No explanation of the joke, no rant, no threat, just a
small household grudge left on the door screen.
"""

import os

# The entry text, kept as one module-level constant so the exact
# competition text lives in a single place and is easy to audit.
# It must stay exactly 122 characters on one line; main() checks
# that before writing, so any accidental edit fails loudly instead
# of silently submitting a different note.
ENTRY_TEXT = (
    "You put the leftovers in on Friday and called it 'meal prep.' "
    "I have been staring at them ever since. They have names now."
)


def main() -> None:
    # Pre-write self-check: the entry must be exactly the approved
    # 122-character single line, with no trailing newline added.
    if len(ENTRY_TEXT) != 122 or "\n" in ENTRY_TEXT:
        raise ValueError(
            f"ENTRY_TEXT must be 122 characters on one line, "
            f"got {len(ENTRY_TEXT)} characters"
        )
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    print(f"Wrote {len(ENTRY_TEXT)} characters to {path}")


if __name__ == "__main__":
    main()
