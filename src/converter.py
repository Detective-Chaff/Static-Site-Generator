from src.textnode import TextNode, TextType
from src.leafnode import LeafNode
import re

class Converter():

    @staticmethod
    def text_node_to_html_node(text_node):
        if isinstance(text_node, TextNode):
            match (text_node.text_type):
                case (TextType.TEXT):
                    return LeafNode(None, text_node.text)
                case (TextType.BOLD):
                    return LeafNode("b", text_node.text)
                case (TextType.ITALICS):
                    return LeafNode("i", text_node.text)
                case (TextType.CODE):
                    return LeafNode("code", text_node.text)
                case (TextType.LINKS):
                    return LeafNode("a", text_node.text, {"href": text_node.url})
                case (TextType.IMAGES):
                    return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
                case _:
                    raise Exception("Text Type not supported")
        else:
            raise Exception("must provide a TextNode type")
    
    @staticmethod
    def split_nodes_delimiter(nodes, delim, type):
        new_nodes = []
        for node in nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
                continue
            split_nodes = []
            sections = node.text.split(delim)
            if len(sections) % 2 == 0:
                raise ValueError("invalid markdown, formatted section not closed")
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(sections[i], TextType.TEXT))
                else:
                    split_nodes.append(TextNode(sections[i], type))
            new_nodes.extend(split_nodes)
        return new_nodes
    
    @staticmethod
    def extract_markdown_images(text):
        pattern = re.compile(r'\!\[([^\[\]]*)\]\(([^\(\)]*)\)')
        result = re.findall(pattern, text)
        return result

    @staticmethod
    def extract_markdown_links(text):
        pattern = re.compile(r'\[([^\[\]]*)\]\(([^\(\)]*)\)')
        result = re.findall(pattern, text)
        return result
    
    @staticmethod
    def split_nodes_img(old_nodes):
        nodes = old_nodes
        new_nodes = []

        if not nodes:
            return new_nodes
        
        for node in nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
                continue

            new_text = node.text
            link_info = Converter.extract_markdown_images(new_text)
            if len(link_info) == 0:
                new_nodes.append(node)
                continue

            for link in link_info:
                t_value, url = link
                link_markdown = f"![{t_value}]({url})"
                start = new_text.find(link_markdown)
                end = start + len(link_markdown)
                if start == 0:
                    new_nodes.append(TextNode(t_value, TextType.IMAGES, url))
                else:
                    new_nodes.append(TextNode(new_text[:start], TextType.TEXT))
                    new_nodes.append(TextNode(t_value, TextType.IMAGES, url))
                new_text = new_text[end:]
            if len(new_text) != 0:
                new_nodes.append(TextNode(new_text,TextType.TEXT))
        return new_nodes
    
    @staticmethod
    def split_nodes_links(old_nodes):
        nodes = old_nodes
        new_nodes = []

        if not nodes:
            return new_nodes
        
        for node in nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
                continue

            new_text = node.text
            link_info = Converter.extract_markdown_links(new_text)
            if len(link_info) == 0:
                new_nodes.append(node)
                continue

            for link in link_info:
                t_value, url = link
                link_markdown = f"[{t_value}]({url})"
                start = new_text.find(link_markdown)
                end = start + len(link_markdown)
                if start == 0:
                    new_nodes.append(TextNode(t_value, TextType.LINKS, url))
                else:
                    new_nodes.append(TextNode(new_text[:start], TextType.TEXT))
                    new_nodes.append(TextNode(t_value, TextType.LINKS, url))
                new_text = new_text[end:]
            if len(new_text) != 0:
                new_nodes.append(TextNode(new_text,TextType.TEXT))
        return new_nodes
    
    @staticmethod
    def text_to_textnodes(text):
        if text == "":
            return text
        node = TextNode(text, TextType.TEXT)
        new_nodes = Converter.split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = Converter.split_nodes_delimiter(new_nodes, "*", TextType.ITALICS)
        new_nodes = Converter.split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        new_nodes = Converter.split_nodes_img(new_nodes)
        new_nodes = Converter.split_nodes_links(new_nodes)

        return new_nodes

                


