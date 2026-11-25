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

NOTE = (
    "You put the leftovers in on Friday and called it 'meal prep.' "
    "I have been staring at them ever since. They have names now."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(NOTE)
    print(f"Wrote {len(NOTE)} characters to {path}")


if __name__ == "__main__":
    main()
