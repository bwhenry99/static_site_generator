import os
import markdowntohtml

def generate_page(from_path, template_path, dest_path):
    print(f"Generating Page from {from_path} to {dest_path} using {template_path}.")
    source_file = open(from_path, mode='r')
    template_file = open(template_path, mode='r')
    markdown = source_file.read()
    template = template_file.read()
    html = markdowntohtml.markdown_to_html_node(markdown).to_html()
    title = markdowntohtml.extract_title(markdown)

    print(template)
    template = template.replace("{{ Title }}", title)
    print(template)
    template = template.replace("{{ Content }}", html)

    dest_file = open(dest_path, mode='w')
    dest_file.write(template)

