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
        in_code_block = False
        for line in f:
            line = line.rstrip()
            if in_code_block:
                if line == "```":
                    html_lines.append("</code></pre>")
                    in_code_block = False
                else:
                    html_lines.append(line)
                continue

            # Check for Markdown headings
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                html_lines.append(f"<h{heading_level}>{heading_text}</h{heading_level}>")
            elif line == "```":
                html_lines.append("<pre><code>")
                in_code_block = True
            else:
                # Check for ordered list items
                if re.match(r"^[0-9]+\. ", line):
                    if not in_ol_list:
                        html_lines.append("<ol>")
                        in_ol_list = True
                    html_lines.append(f"<li>{line.split(' ', 1)[1]}</li>")
                else:
                    if in_ol_list:
                        html_lines.append("</ol>")
                        in_ol_list = False
                    # Check for unordered list items
                    if re.match(r"^[\*\-\+] ", line):
                        if not in_ul_list:
                            html_lines.append("<ul>")
                            in_ul_list = True
                        html_lines.append(f"<li>{line[2:].strip()}</li>")
                    else:
                        if in_ul_list:
                            html_lines.append("</ul>")
                            in_ul_list = False
                        # Convert inline code
                        line = re.sub(r"`([^`]*)`", r"<code>\1</code>", line)
                        if line:
                            html_lines.append(f"<p>{line}</p>")

        # Close any open list at the end of the file
        if in_ol_list:
            html_lines.append("</ol>")
        if in_ul_list:
            html_lines.append("</ul>")
        if in_code_block:
            html_lines.append("</code></pre>")

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
