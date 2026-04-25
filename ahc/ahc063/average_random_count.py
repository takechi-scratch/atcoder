#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


RANDOM_COUNT_PATTERN = re.compile(r"random_count\s*=\s*([-+]?(?:\d+\.?\d*|\.\d+))")


def extract_random_counts(file_path: Path) -> list[float]:
    values: list[float] = []
    try:
        text = file_path.read_text(encoding="utf-8", errors="ignore")
    except OSError as e:
        print(f"[WARN] Failed to read {file_path}: {e}")
        return values

    for line in text.splitlines():
        for match in RANDOM_COUNT_PATTERN.finditer(line):
            values.append(float(match.group(1)))
    return values


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Search *.txt files under a directory and compute the average of random_count values."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Target directory to search recursively (default: current directory)",
    )
    args = parser.parse_args()

    root = Path(args.directory)
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"[ERROR] Directory not found: {root}")

    all_values: list[float] = []
    txt_files = sorted(root.rglob("*.txt"))

    for txt_file in txt_files:
        all_values.extend(extract_random_counts(txt_file))

    if not txt_files:
        print("No .txt files found.")
        return

    if not all_values:
        print("No random_count values found.")
        return

    average = sum(all_values) / len(all_values)
    print(f"txt_files_scanned={len(txt_files)}")
    print(f"random_count_values_found={len(all_values)}")
    print(f"average_random_count={average}")


if __name__ == "__main__":
    main()
