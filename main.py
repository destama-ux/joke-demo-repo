"""Entry for make.fun's "The joke about the demo" bounty.

Writes one one-line joke about working beside AI coding agents to
entry.txt in the output directory (MAKEFUN_OUTPUT_DIR, else /output).
No network, standard library only.
"""

import os

JOKE = (
    "My AI pair programmer never argues, never sleeps, and never remembers "
    "writing the bug it is now confidently explaining to me as legacy code."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(JOKE + "\n")


if __name__ == "__main__":
    main()
