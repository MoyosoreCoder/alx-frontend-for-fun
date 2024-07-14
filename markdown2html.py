#!/usr/bin/python3
"""
This is a script to convert a Markdown file to HTML.
Arguments:
    - First argument: the name of the Markdown file
    - Second argument: the output file name
If the number of arguments is less than 2:
    Output: Usage: ./markdown2html.py README.md README.html
    Exit with status 1
If the Markdown file doesn’t exist:
    Output: Missing <filename>
    Exit with status 1
Otherwise:
    Convert the Markdown file to HTML, print nothing, and exit with status 0
"""

import sys
import os
import markdown

def print_usage_and_exit():
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

def print_missing_and_exit(filename):
    print(f"Missing {filename}", file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    # Check if the number of arguments is less than 2
    if len(sys.argv) != 3:
        print_usage_and_exit()

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.exists(md_file):
        print_missing_and_exit(md_file)

    # Read the Markdown file
    with open(md_file, 'r') as f:
        md_content = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Write the HTML content to the output file
    with open(html_file, 'w') as f:
        f.write(html_content)

    # Exit with success
    sys.exit(0)

