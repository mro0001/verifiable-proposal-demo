"""Write a step's results as a small table of key and value, with word forms.

Purpose:
    Give both step scripts one way to write their results. Each result is one
    row of key and value. Rows are sorted by key, so a rerun writes the same
    bytes. A number the appendix writes as a word gets a second row, whose key
    ends in .word, or in .word_cap when the word starts a sentence.
Assumptions:
    Word forms are written for whole numbers from zero to twelve. A larger
    number keeps its digits in the word row, which a reader would notice in the
    built text. Standard library only, so the pipeline replays anywhere.
"""
import csv

WORDS = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
         "ten", "eleven", "twelve")


def word(value):
    """Return the English word for a whole number from zero to twelve, else its digits."""
    n = int(value)
    if 0 <= n < len(WORDS):
        return WORDS[n]
    return str(n)


def add_words(results, keys, cap_keys):
    """Add a .word row for each key in keys and a .word_cap row for each key in cap_keys."""
    for key in keys:
        results[key + ".word"] = word(results[key])
    for key in cap_keys:
        text = word(results[key])
        results[key + ".word_cap"] = text[:1].upper() + text[1:]


def write_rows(name, results):
    """Write results, a dict of key to value, to the CSV file name, one row per key, sorted."""
    with open(name, "w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["key", "value"])
        for key in sorted(results):
            writer.writerow([key, results[key]])
