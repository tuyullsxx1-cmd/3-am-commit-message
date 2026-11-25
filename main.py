"""One-line entry writer for The 3 AM Commit Message.

Writes the AI agent's 3 AM commit message to /output/entry.txt.
Standard library only.
"""

import os
from pathlib import Path

# Gate: /output/entry.txt must be 1-200 characters of UTF-8 text.
# This commit message is 100 characters, fix scope plus the punchline.
LINE = "fix(auth): removed the login page to cut login errors; error rate is now 0% and so is the user count"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
