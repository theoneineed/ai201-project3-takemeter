import csv
import re
from pathlib import Path

FILES = ["./data/seekAdvice.txt", "./data/provideValue.txt", "./data/validateOneself.txt"]
OUTPUT_CSV = "./data/trainExamples.csv"

def clean_line(line: str) -> str:
    """
    Removes leading numbering like '1. ', '23. ', etc.
    """
    return re.sub(r"^\s*\d+\.\s*", "", line).strip()

rows = []

for file_name in FILES:
    label = Path(file_name).stem  # e.g., seekAdvice.txt -> seekAdvice

    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            cleaned = clean_line(line)

            if cleaned:
                rows.append({
                    "Text": cleaned,
                    "Label": label,
                    "Notes": ""
                })

# Write to CSV
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Text", "Label", "Notes"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

print(f"Saved {len(rows)} rows to {OUTPUT_CSV}")