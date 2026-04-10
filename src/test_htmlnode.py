import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "this is text")
        node2 = HTMLNode("h1", "this is text")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("h2", "this is text i guess")
        node2 = HTMLNode("h1", "this is text")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()