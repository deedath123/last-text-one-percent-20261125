"""Last Text at One Percent: a dying phone's final message at 1% battery.

The phone spends its last charge on one last text to its owner.
The joke is a parting gift disguised as sabotage: on its way out, the phone murders the morning alarm, so its owner gets to sleep in.
"""

import os

ENTRY = "I'm at 1%, so this is my last text: I already deleted your 6 a.m. alarm. It dies with me. Sleep in. You're welcome."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
