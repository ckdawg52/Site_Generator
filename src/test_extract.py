import unittest

from textnode import TextNode, TextType
from extract import extract_markdown_images, extract_markdown_links, extract_title

class TestTextNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](www.google.com)"
        )
        self.assertListEqual([("link", "www.google.com")], matches)

    def test_2_links(self):
        matches = extract_markdown_links("This is the first [link](www.google.com) and another [one](www.youtube.com)")
        self.assertListEqual([("link", "www.google.com"), ("one", "www.youtube.com")], matches)

    def test_extract_title(self):
        title = extract_title("# This is a title")
        self.assertEqual("This is a title", title)

    def test_extract_title2(self):
        try:
            title = extract_title("## This is a title")
        except:
            return
        self.assertNotEqual("This is a title", title)

    def test_extract_title3(self):
        try:
            title = extract_title("This is not a title")
        except:
            return
        self.assertNotEqual("This is a title", title)



if __name__ == "__main__":
    unittest.main()