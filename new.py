#!/usr/bin/python3
"""
A script that converts Markdown to HTML.
"""

import sys
import os

def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML and writes the output to a file.
    """
    with open(input_file, "r", encoding="utf-8") as f:
        markdown_lines = f.readlines()

    html_lines = []
    for line in markdown_lines:
        line = line.rstrip()
        if line.startswith("#"):
            heading_level = len(line.split(" ")[0])
            heading_text = line[heading_level + 1:]
            html_lines.append(f"<h{heading_level}>{heading_text}</h{heading_level}>")
        elif line.startswith("- "):
            html_lines.append(f"<li>{line[2:]}</li>")
        else:
            if line.strip():
                html_lines.append(f"<p>{line}</p>")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)

