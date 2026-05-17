from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "pargraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleanBlocks = []


    for block in blocks:
        if block == "":
            continue
        cleaned = block.strip()
        cleanBlocks.append(cleaned)

    return cleanBlocks

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    lines = block.split('\n')
    index = 1
    quote = True
    unorderedList = True
    orderedList = True

    for line in lines:
        if not line:
            continue

        if not line.startswith(">"):
            quote = False
        if not line.startswith("- "):
            unorderedList = False
        if not line.startswith(f"{index}. "):
            orderedList = False
        index += 1
        
    if quote:
        return BlockType.QUOTE
    if unorderedList:
        return BlockType.UNORDERED_LIST
    if orderedList:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH