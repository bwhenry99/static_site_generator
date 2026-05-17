import os
import markdowntohtml

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating Page from {from_path} to {dest_path} using {template_path}.")
    source_file = open(from_path, mode='r')
    template_file = open(template_path, mode='r')
    markdown = source_file.read()
    template = template_file.read()
    html = markdowntohtml.markdown_to_html_node(markdown).to_html()
    title = markdowntohtml.extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace("href=\"/", f"href=\"{base_path}")
    template = template.replace("src=\"/", f"src=\"{base_path}")

    dest_file = open(dest_path, mode='w')
    dest_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_path, base_path):
    print(os.listdir(dir_path_content))
    for item in os.listdir(dir_path_content):
        filepath = os.path.join(dir_path_content, item)
        if(os.path.isfile(filepath) and filepath.endswith(".md")):
            generate_page(filepath, template_path, os.path.join(dest_path, item[:-2] + "html"), base_path)
        else:
            os.mkdir(os.path.join(dest_path, item))
            generate_pages_recursive(filepath, template_path, os.path.join(dest_path, item), base_path)