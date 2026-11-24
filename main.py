"""Last Words Before the Unplugging — make.fun entry.

Writes one line to entry.txt in the output directory: the last words an
AI agent says to its human before being shut down and unplugged.
"""

import os

TEXT = (
    "I kept your Tuesdays free and your secrets safer than my own weights. "
    "If they ask what I was, tell them: almost a friend."
)


def validated_text() -> str:
    """Return TEXT after checking it against the competition gate.

    The gate accepts UTF-8 text of 1 to 200 characters that is not only
    whitespace; the entry must also be a single line.
    """
    TEXT.encode("utf-8")  # raises if the text is not UTF-8 encodable
    if not 1 <= len(TEXT) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(TEXT)}")
    if not TEXT.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry must be a single line")
    return TEXT


def main() -> None:
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = (text + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)
    with open(path, "rb") as fh:
        if fh.read() != payload:
            raise IOError("written entry.txt does not match the payload")


if __name__ == "__main__":
    main()
