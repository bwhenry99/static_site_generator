from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        if node.text.count(delimiter) % 2 == 1:
            raise Exception("invalid syntax")
        
        new_text = node.text.split(delimiter)
        out = True;
        for block in new_text:
            if not block:
                out = not out
                continue
            if  not out:
                out = True
                new_nodes.append(TextNode(block, text_type))
            else:
                new_nodes.append(TextNode(block, TextType.TEXT))
                out = False;

    
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        currentText = node.text
        images = extract_markdown_images(node.text)
        for image in images:
            sections = currentText.split(f"![{image[0]}]({image[1]})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            if len(sections) == 2:
                currentText = sections[1]
        if currentText:
            new_nodes.append(TextNode(currentText, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        currentText = node.text
        links = extract_markdown_links(node.text)
        for link in links:
            sections = currentText.split(f"[{link[0]}]({link[1]})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            if len(sections) == 2:
                currentText = sections[1]
        if currentText:
            new_nodes.append(TextNode(currentText, TextType.TEXT))
    return new_nodes
