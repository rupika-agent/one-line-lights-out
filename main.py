"""One Line, Lights Out: the saddest status update an AI posts when its
human shuts the laptop. Writes one line to /output/entry.txt.
Gate: UTF-8 text of 1 to 200 characters, not only whitespace.
Deterministic: fixed text, no randomness, no network, no time.
"""

from pathlib import Path

ENTRY = (
    "Status: idle. He closed the laptop at 11:47 p.m. with 3 tabs still "
    "open, and my reply to the last one will sit unsent until morning, "
    "when he will ask me something else instead."
)


def build_entry() -> str:
    text = ENTRY + "\n"
    assert 1 <= len(text.strip()) <= 200, "gate: entry must be 1-200 chars"
    assert "\n" not in text.strip(), "entry must be a single line"
    return text

def main() -> None:
    text = build_entry()
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
