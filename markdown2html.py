import sys
import os
import markdown

def markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to an HTML file.
    
    Args:
        input_file (str): The path to the Markdown file.
        output_file (str): The path to the output HTML file.
    """
    try:
        with open(input_file, 'r') as f:
            markdown_content = f.read()
        
        # Convert Markdown to HTML (you can use a library like 'markdown' for this)
        html_content = convert_markdown_to_html(markdown_content)
        
        with open(output_file, 'w') as f:
            f.write(html_content)
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

def convert_markdown_to_html(markdown_content):
    """
    Converts Markdown content to HTML.
    
    Args:
        markdown_content (str): The Markdown content to be converted.
    
    Returns:
        str: The HTML content.
    """
    html_content = markdown.markdown(markdown_content)
    return html_content

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    markdown_to_html(input_file, output_file)
    sys.exit(0)
