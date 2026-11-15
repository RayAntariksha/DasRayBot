import csv

import config


def load_friends():
    """Return (fieldnames, rows). Raises FileNotFoundError if missing."""
    with open(config.FRIENDS_CSV, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, skipinitialspace=True)
        return reader.fieldnames, list(reader)


def save_friends(fieldnames, rows):
    with open(config.FRIENDS_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
