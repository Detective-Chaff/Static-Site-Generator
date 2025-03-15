from pydoc import text
from parentnode import ParentNode
from textnode import TextNode, TextType
from leafnode import LeafNode
from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    U_LIST = "unordered_list"
    O_LIST = "ordered_list"

class Converter():

    @staticmethod
    def text_node_to_html_node(text_node):
        # if isinstance(text_node, TextNode):
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
                return LeafNode("img", " ", {"src": text_node.url, "alt": text_node.text})
            case _:
                raise Exception("Text Type not supported")
        # else:
        #     raise Exception("must provide a TextNode type")
    
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
        pattern = re.compile(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)')
        result = re.findall(pattern, text)
        return result

    @staticmethod
    def extract_markdown_links(text):
        pattern = re.compile(r'\[([^\[\]]*)\]\(([^\(\)]*)\)')
        result = re.findall(pattern, text)
        return result
    
    @staticmethod
    def split_nodes_img(old_nodes):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
                continue
            new_text = node.text
            imgs = Converter.extract_markdown_images(new_text)
            if len(imgs) == 0:
                new_nodes.append(node)
                continue
            for img in imgs:
                blocks = new_text.split(f"![{img[0]}]({img[1]})", 1)
                if len(blocks) != 2:
                    raise ValueError("invalid markdown, image section not closed")
                if blocks[0] != "":
                    new_nodes.append(TextNode(blocks[0], TextType.TEXT))
                new_nodes.append(TextNode(img[0], TextType.IMAGES, img[1],))
                new_text = blocks[1]
            if new_text != "":
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
        # if text == "":
        #     return text
        new_nodes = [TextNode(text, TextType.TEXT)]
        new_nodes = Converter.split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        new_nodes = Converter.split_nodes_delimiter(new_nodes, "*", TextType.ITALICS)
        new_nodes = Converter.split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        new_nodes = Converter.split_nodes_img(new_nodes)
        new_nodes = Converter.split_nodes_links(new_nodes)
        return new_nodes

    @staticmethod    
    def markdown_to_blocks(markdown):
        stripped = []
        if len(markdown) == 0 or markdown == " ":
            return stripped
        segments = markdown.split('\n\n')
        stripped = list(filter(lambda x: None if x == "" else x, list(map(lambda x: x.lstrip().rstrip(),segments))))
        return stripped

    @staticmethod
    def block_to_blocktype(block):
        if not block:
            return block
        
        # Code Block
        if block[:3] == "```" and block[-3:] == "```":
            return BlockType.CODE
        
        # Heading
        heading = r'^(#{1,6}\s)+'
        pattern = re.compile(heading)
        match = pattern.match(block)
        if match:
            return BlockType.HEADING
        
        # Unordered List
        ul = r'^[\*-] |\r?\\n?[\*-] '
        pattern = re.compile(ul)
        match = pattern.match(block)
        if match:
            return BlockType.U_LIST
        
        #Quote
        quote = r'^>|\r?\\n?>'
        pattern = re.compile(quote)
        match = pattern.match(block)
        if match:
            return BlockType.QUOTE
        
        # Ordered List
        if block.startswith("1. "):
            start = 1
            lines = block.split("\n")
            for line in lines:
                if line.startswith(f"{start}. "):
                    start += 1
                    continue
                else:
                    return BlockType.PARAGRAPH
            return BlockType.O_LIST
        
        return BlockType.PARAGRAPH
        
    @staticmethod
    def markdown_to_html_node(in_markdown):
        # 1. check markdown isn't empty
        if not in_markdown:
            raise Exception("markdown is empty")
        blocks = Converter.markdown_to_blocks(in_markdown)
        parent = []
        for block in blocks:
            block_type = Converter.block_to_blocktype(block)
            match(block_type):
                case (BlockType.PARAGRAPH):
                    parent.append(Converter.create_paragrpah(block))
                case(BlockType.HEADING):
                    parent.append(Converter.create_heading(block))
                case(BlockType.CODE):
                    parent.append(Converter.create_codeblock(block))
                case(BlockType.QUOTE):
                    parent.append(Converter.create_block_quote(block))
                case(BlockType.U_LIST):
                    parent.append(Converter.create_unordered_list(block))
                case(BlockType.O_LIST):
                    parent.append(Converter.create_ordered_list(block))
        return ParentNode("div", parent)

    def text_to_children(text):
        text_nodes = Converter.text_to_textnodes(text)
        children = []
        for text_node in text_nodes:
            html_node = Converter.text_node_to_html_node(text_node)
            children.append(html_node)
        return children
    
    def create_paragrpah(text):
        lines = text.split("\n")
        line = " ".join(lines)
        html_nodes = Converter.text_to_children(line)
        return ParentNode("p", html_nodes)
        

    def create_unordered_list(block):
        item_list = []
        ul = []
        items = block.split("\n")
        for item in items:
            item = item[2:]
            item_list = Converter.text_to_children(item)
            ul.append(ParentNode("li", item_list))

        return ParentNode("ul", ul)
    
    def create_ordered_list(block):
        ol =[]
        items = block.split("\n")
        for item in items:
            item = item[3:]
            item_list = Converter.text_to_children(item)
            ol.append(ParentNode("li", item_list))
        return ParentNode("ol", ol)
            
    def create_heading(text):
        markers = text.count("#")
        stripped = text[markers + 1:]
        line = Converter.text_to_children(stripped)
        return ParentNode(f"h{markers}", line)
    
    def create_codeblock(text):
        nodes = []
        code_nodes = []
        stripped = text.lstrip("```").rstrip("```")
        lines = stripped.split("\n")
        main_line = ""
        for line in lines:
            main_line += line.lstrip().rstrip()
        code_nodes = Converter.text_to_children(main_line)
        nodes.append(ParentNode("code", code_nodes)) 
        return ParentNode("pre", nodes)

    def create_block_quote(text):
        lines = text.split("\n")

        quote_lines = []
        sentence = ""
        for line in lines:
            sentence += f" {line[2:]}"
        quote_lines = Converter.text_to_children(sentence.lstrip().rstrip())
        return ParentNode("blockquote", quote_lines)




