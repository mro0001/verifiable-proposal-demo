"""Tidy pandoc's docx to markdown output of the technical appendix. Python 3.9.

Usage: docx_to_md.py IN.md OUT.md

This is the appendix converter used for the October 27 drafts (113_docx_to_md.py
in the proposal's working folder), with one change. It keeps pandoc's escapes of
\\[, \\] and \\@, so the literal [@nakamura2020] and @nakamura2020 in the example
report stay plain text and are not read as citations (fix 2 of the conversion).
The figure lines are pointed at their files by fix_figs.py, and the table widths
are set from the Word file by table_widths.py.

What it does
- straight quotes for curly ones, a plain space for a no-break space, ... for the
  ellipsis character (pandoc prints them curly again on the way back to Word)
- every table separator line written as |---|---|, ready for table_widths.py
- a nested list item indented four spaces
- an indented code block written as a fenced one
- the example report in A2.5 wrapped in the Report Text style
"""
import re
import sys

SEP = re.compile(r"^\|(-+\|)+\s*$")
REPORT_START = "**Citation verification report**"
REPORT_END = "*\\[6 notes omitted\\]*"


def norm(text):
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    text = text.replace(" ", " ").replace("…", "...").replace("|  |", "| |")
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        line = lines[i]
        if SEP.match(line):
            line = "|" + "---|" * (line.count("|") - 1)
        if re.match(r"^  - ", line):
            line = "  " + line
        if line.startswith("    ") and not line.lstrip().startswith("- ") and (not out or out[-1] == ""):
            block = []
            while i < len(lines) and (lines[i].startswith("    ") or (
                    lines[i] == "" and i + 1 < len(lines) and lines[i + 1].startswith("    "))):
                block.append(lines[i][4:])
                i += 1
            out.append("```")
            out.extend(block)
            out.append("```")
            continue
        out.append(line)
        i += 1
    text = "\n".join(out)
    if REPORT_START not in text or REPORT_END not in text:
        raise SystemExit("the example report's first or last line was not found")
    a = text.index(REPORT_START)
    b = text.index(REPORT_END) + len(REPORT_END)
    return text[:a] + '::: {custom-style="Report Text"}\n\n' + text[a:b] + "\n\n:::" + text[b:]


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf8") as handle:
        text = handle.read()
    with open(dst, "w", encoding="utf8") as handle:
        handle.write(norm(text))
