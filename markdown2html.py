#!/usr/bin/env python3

import sys
import os
import mistletoe

def main():
    """
    Main function that handles the conversion of a Markdown file to HTML.
    
    Steps:
    1. Check if the number of arguments is less than 2.
    2. Get the input and output file names from the arguments.
    3. Check if the input file exists.
    4. Read the content of the input Markdown file.
    5. Convert the Markdown content to HTML.
    6. Write the HTML content to the output file.
    7. Exit with the appropriate status.
    """
    # Checking if the number of arguments is less than 2
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Geting the input and output file names
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Checking if the Markdown file exists
    if not os.path.exists(input_filename):
        print(f"Missing {input_filename}", file=sys.stderr)
        sys.exit(1)

    # Reading the Markdown file
    with open(input_filename, 'r') as input_file:
        markdown_text = input_file.read()

    # Converting Markdown to HTML
    html_text = mistletoe.markdown(markdown_text)

    # Writing the HTML to the output file
    with open(output_filename, 'w') as output_file:
        output_file.write(html_text)

    # Exiting successfully
    sys.exit(0)

if __name__ == "__main__":
    main()

