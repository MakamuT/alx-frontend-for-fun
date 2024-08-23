#!/usr/bin/env python3
"""
takes an argument 2 strings
"""
import markdown
import os
import sys

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

markdown_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

with open(markdown_file, 'r') as mark_file:
    markdown_text = mark_file.read()

html = markdown.markdown(markdown_text)

with open(output_file) as html_file:
    html_file.write(html)
sys.exit(0)
