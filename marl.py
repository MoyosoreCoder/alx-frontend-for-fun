#!/usr/bin/python3
"""
A script that converts Markdown to HTML.
"""

import sys
import os
import re


def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML and writes the output to a file.
    """
    with open(input_file, encoding="utf-8") as f:
        html_lines = []
        in_ol_list = False
        in_ul_list = False
        paragraph_lines = []

        def close_paragraph():
            if paragraph_lines:
                html_lines.append("<p>")
                for idx, pline in enumerate(paragraph_lines):
                    if idx > 0:
                        html_lines.append("    <br />")
                    html_lines.append("    " + pline)
                html_lines.append("</p>")
                paragraph_lines.clear()

        for line in f:
            line = line.rstrip()

            # Check for Markdown headings
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                close_paragraph()
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                html_lines.append(f"<h{heading_level}>{heading_text}</h{heading_level}>")
            else:
                # Check for ordered list items
                if line.startswith("* "):
                    close_paragraph()
                    if not in_ol_list:
                        html_lines.append("<ol>")
                        in_ol_list = True
                    html_lines.append(f"<li>{line[2:].strip()}</li>")
                else:
                    if in_ol_list:
                        html_lines.append("</ol>")
                        in_ol_list = False
                    # Collect paragraph lines
                    if line:
                        paragraph_lines.append(line)
                    else:
                        close_paragraph()

        # Close any open list at the end of the file
        if in_ol_list:
            html_lines.append("</ol>")
        # Close any remaining open paragraph
        close_paragraph()

    # Write the HTML output to a file
    with open(output_file, "w", encoding="utf-8") as f:
        for line in html_lines:
            f.write(line + "\n")


if __name__ == "__main__":
    # Check that the correct number of arguments were provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Get the input and output file names from the command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check that the Markdown file exists and is a file
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Convert the Markdown file to HTML and write the output to a file
    convert_markdown_to_html(input_file, output_file)

    # Exit with a successful status code
    sys.exit(0)
