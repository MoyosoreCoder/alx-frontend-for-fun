#!/usr/bin/python3
"""
This script takes two arguments: the first is a markdown file name and the
second is an HTML output filename.
Requirements:
    - If the number of arguments is less than 2: print in STDERR Usage: ./markdown2html.py README.md README.html and exit 1
    - If the Markdown file doesn’t exist: print in STDERR Missing <filename> and exit 1
    - Otherwise, print nothing and exit 0
"""

import sys
import os
import markdown

if __name__ == '__main__':
    # Check if the number of arguments is less than 2
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(md_file):
        print(f'Missing {md_file}', file=sys.stderr)
        sys.exit(1)

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

