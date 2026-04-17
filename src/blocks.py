from enum import Enum

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    output = []
    for block in blocks:
        block = block.strip()
        if block != "":
            output.append(block)
    return output

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    if markdown.startswith("#"):
        return BlockType.HEADING
    if markdown.startswith("```"):
        return BlockType.CODE
    if markdown.startswith("> "):
        return BlockType.QUOTE
    if markdown.startswith("- "):
        return BlockType.UNORDERED_LIST
    if markdown.startswith("1. "):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH