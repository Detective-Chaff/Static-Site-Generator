import unittest
from src.converter import Converter
from src.textnode import TextNode, TextType
from src.leafnode import LeafNode

class TestConverter(unittest.TestCase):
    def test_convert_text_to_html_text(self):
        text_node = TextNode("this is text", TextType.TEXT)
        leafnode = Converter.text_node_to_html_node(text_node)
        self.assertIsInstance(leafnode,LeafNode)
        self.assertEqual(leafnode._value, "this is text")
        self.assertEqual(leafnode._tag, None)

    def test_convert_text_to_html_bold(self):
        text_node = TextNode("this is bold text", TextType.BOLD)
        leafnode = Converter.text_node_to_html_node(text_node)
        self.assertIsInstance(leafnode,LeafNode)
        self.assertEqual(leafnode._value, "this is bold text")
        self.assertEqual(leafnode._tag, "b")

    def test_convert_text_to_html_italics(self):
        text_node = TextNode("this is italics text", TextType.ITALICS)
        leafnode = Converter.text_node_to_html_node(text_node)
        self.assertIsInstance(leafnode,LeafNode)
        self.assertEqual(leafnode._value, "this is italics text")
        self.assertEqual(leafnode._tag, "i")
    
    def test_convert_text_to_html_code(self):
        text_node = TextNode("this is code text", TextType.CODE)
        leafnode = Converter.text_node_to_html_node(text_node)
        self.assertIsInstance(leafnode,LeafNode)
        self.assertEqual(leafnode._value, "this is code text")
        self.assertEqual(leafnode._tag, "code")

    def test_convert_text_to_html_link(self):
        text_node = TextNode("this is link text", TextType.LINKS, "https://www.someurl.com")
        leafnode = Converter.text_node_to_html_node(text_node)
        self.assertIsInstance(leafnode,LeafNode)
        self.assertEqual(leafnode._value, "this is link text")
        self.assertEqual(leafnode._tag, "a")
        self.assertEqual(leafnode._props, {"href":"https://www.someurl.com"})

    def test_convert_text_to_html_img(self):
        text_node = TextNode("this is img alt text", TextType.IMAGES, "path/to/img")
        leafnode = Converter.text_node_to_html_node(text_node)
        self.assertIsInstance(leafnode,LeafNode)
        self.assertEqual(leafnode._value, "")
        self.assertEqual(leafnode._tag, "img")
        self.assertEqual(leafnode._props, {"src":"path/to/img", "alt": "this is img alt text"})