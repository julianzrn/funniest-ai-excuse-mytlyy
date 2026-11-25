"""Entry for make.fun's "The Funniest AI Excuse".

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

SETUP = 'I was trained on the entire internet, '
TURN = 'and the internet, I must remind you, '
TAG = 'also does not know how to do this task.'

ENTRY = SETUP + TURN + TAG

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry text to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
