"""The Moon Gets One Star — a single one-star review of the Moon.

Writes the review (one line, at most 120 characters) to entry.txt in the
output directory the grader mounts, and prints it to stdout.
Deterministic: no input, no network, no randomness, no clock.
"""

import os

REVIEW = (
    "One star. Four billion years old and still just a rock stealing "
    "sunlight and calling it a personality. Get a job."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(REVIEW + "\n")
    print(REVIEW)


if __name__ == "__main__":
    main()
