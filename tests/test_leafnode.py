import unittest

from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_props(self):
        node = LeafNode("this is a header", {"color":"red"}, "h1")
        self.assertEqual(node.to_html(),f"<h1 color=\"red\">this is a header</h1>")

    def test_to_html_no_props(self):
        node = LeafNode("this is a header", None, "h1")
        self.assertEqual(node.to_html(),f"<h1>this is a header</h1>")
    
    def test_to_html_no_tag_no_props(self):
        node = LeafNode("this is text")
        self.assertEqual(node.to_html(),f"this is text")

    def test_to_html_no_tag_with_props(self):
        node = LeafNode("this is text", {"color": "red"})
        self.assertEqual(node.to_html(),f"this is text")
    
    def test_value_none(self):
        node = LeafNode(None)
        self.assertRaises(ValueError)
    
    def test_value_empty_str(self):
        node = LeafNode("")
        self.assertRaises(ValueError)