"""Cat review entry: one original one-star review by a house cat.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The review is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.

The review keeps the deadpan shape of a real one-star review while the
complaint goes somewhere only a cat would go: the human asked the vet
whether the cat is "too independent", so the cat answers with an overnight
stare from his chest. The sting lands in the last sentence.
"""

import os


JOKE = (
    "One star. He asked the vet if I am 'too independent'. I waited until "
    "he fell asleep, then sat on his chest and stared at him until morning. "
    "He has stopped asking."
)

OUTPUT_PATH = "/output/entry.txt"

# The competition gate: 1 to 200 characters, not whitespace-only, one line.
MAX_CHARS = 200


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "review must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text:
        # A review with a line break is not a single line, so refuse it
        # here instead of letting the gate reject the entry.
        raise SystemExit("review must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = text.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the review.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the review")
    print(text)


if __name__ == "__main__":
    main()
