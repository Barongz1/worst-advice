"""Worst AI Advice — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one line of the worst possible advice an AI could give, at most 140 characters.
"""
import os

LINE = "To fix your slow computer, just delete System32 — it's only there to slow you down."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
