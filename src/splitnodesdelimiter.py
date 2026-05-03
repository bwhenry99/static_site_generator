from textnode import TextNode, TextType

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