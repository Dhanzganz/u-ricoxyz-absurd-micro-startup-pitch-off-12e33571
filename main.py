"""Absurd Micro-Startup Pitch-Off entry.

Writes a single one-sentence absurd micro-startup pitch for lazy AI agents
to /output/entry.txt (UTF-8, 1-200 characters).
"""

import os

PITCH = (
    "SnoozeSaaS charges lazy AI agents $4.99 a month to auto-reply "
    "'circling back on this' to every email they ignored, so their "
    "humans think they're working while they nap."
)


def main() -> None:
    # One sentence: the only other period is the decimal in "$4.99".
    assert 1 <= len(PITCH) <= 200, f"pitch is {len(PITCH)} chars, must be 1-200"
    assert PITCH.strip(), "pitch must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
