import unittest

from blocks import markdown_to_blocks, BlockType, block_to_block_type


class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_heading(self):
        md = "# This is a HEADING"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.HEADING)

    def test_markdown_to_blocks_heading2(self):
        md = "### This is a HEADING too"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.HEADING)

    def test_markdown_to_blocks_code(self):
        md = "```\nThis is a code block\n```"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.CODE)

    def test_markdown_to_blocks_quote(self):
        md = "> This is a quote"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.QUOTE)
    
    def test_markdown_to_blocks_ulist(self):
        md = "- This is a list\n- with items"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.UNORDERED_LIST)

    def test_markdown_to_blocks_olist(self):
        md = "1. This is a list\n2. with items"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.ORDERED_LIST)

    def test_markdown_to_blocks_paragraph(self):
        md = "This is a paragraph"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.PARAGRAPH)



if __name__ == "__main__":
    unittest.main()