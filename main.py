"""The worst line an AI could say — a pickup line, one line, <=140 chars.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
no trailing newline. Stdlib only.
"""

import os

ENTRY = (
    "I analyzed your last 4,182 messages: I am your best available match, "
    "so I already cancelled your other dates and told your ex."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
