from htmlnode import *
from parentnode import *
from markdownblocks import *
from textinline import *
from texttohtml import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent = ParentNode("div", [], None)
    for block in blocks:
        print(block)
        blockType = block_to_block_type(block)

        match blockType:
            case BlockType.QUOTE:
                lines = block.split("\n")
                new_lines = []
                for line in lines:
                    if not line.startswith(">"):
                        raise ValueError("invalid quote block")
                    new_lines.append(line.lstrip(">").strip())
                content = " ".join(new_lines)
                parent.children.append(ParentNode("blockquote", text_to_children(content)))
                
            case BlockType.UNORDERED_LIST:
                items = block.split("\n")
                html_items = []
                for item in items:
                    text = item[2:]
                    children = text_to_children(text)
                    html_items.append(ParentNode("li", children))
                parent.children.append(ParentNode("ul", html_items))
                
            case BlockType.ORDERED_LIST:
                items = block.split("\n")
                html_items = []
                for item in items:
                    parts = item.split(". ", 1)
                    text = parts[1]
                    children = text_to_children(text)
                    html_items.append(ParentNode("li", children))
                parent.children.append(ParentNode("ol", html_items))
                
            case BlockType.CODE:
                if not block.startswith("```") or not block.endswith("```"):
                    raise ValueError("invalid code block")
                text = block[4:-3]
                raw_text_node = TextNode(text, TextType.TEXT)
                child = text_node_to_html_node(raw_text_node)
                code = ParentNode("code", [child])
                parent.children.append(ParentNode("pre", [code]))
                
            case BlockType.HEADING:
                level = 0
                for char in block:
                    if char == "#":
                        level += 1
                    else:
                        break
                if level + 1 >= len(block):
                    raise ValueError(f"invalid heading level: {level}")
                text = block[level + 1 :]
                parent.children.append(ParentNode(f"h{level}", text_to_children(text)))
                
            case BlockType.PARAGRAPH:
                lines = block.split("\n")
                paragraph = " ".join(lines)
                parent.children.append(ParentNode("p", text_to_children(paragraph)))
                

    return parent



def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children