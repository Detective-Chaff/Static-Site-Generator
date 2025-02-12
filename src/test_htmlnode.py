import unittest
from htmlnode import HTMLnode

class TestHtmlNode(unittest.TestCase):
    def test_props(self):
        node = HTMLnode("h1", "something", props={"href": "myHref", "class": "myClass"})
        self.assertEqual(node.props_to_html()," href=myHref class=myClass")
    
    def test_tostring(self):
        node = HTMLnode("p", "test paragraph")
        self.assertEqual(node.__repr__(),"HTMLnode(tag: p, value: test paragraph, children: None, props: None)")
    
    def test_all_properties_none(self):
        node = HTMLnode()
        self.assertIsNone(node.get_tag())
        self.assertIsNone(node.get_value())
        self.assertIsNone(node.get_children())
        self.assertIsNone(node.get_props())