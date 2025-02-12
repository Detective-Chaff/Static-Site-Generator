
from typing import Text
import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_url_none(self):
        none_node = TextNode("", TextType.ITALICS)
        self.assertIsNone(none_node.url)
    
    def test_url_not_none(self):
        url_node = TextNode("url node", TextType.LINKS, "https://someurl.com")
        self.assertIsNotNone(url_node.url)
    
    # This Test should fail
    def test_diff_type(self):
        type_node1 = TextNode("type diff", TextType.BOLD)
        type_node2 = TextNode("type diff", TextType.LINKS)
        self.assertNotEqual(type_node1, type_node2)

    
if __name__ == "__main__":
    unittest.main()