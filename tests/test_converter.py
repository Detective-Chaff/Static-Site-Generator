import unittest
from src.converter import BlockType, Converter
from src.textnode import TextNode, TextType
from src.leafnode import LeafNode

class TestConverter(unittest.TestCase):
#     def test_convert_text_to_html_text(self):
#         text_node = TextNode("this is text", TextType.TEXT)
#         leafnode = Converter.text_node_to_html_node(text_node)
#         self.assertIsInstance(leafnode,LeafNode)
#         self.assertEqual(leafnode._value, "this is text")
#         self.assertEqual(leafnode._tag, None)

#     def test_convert_text_to_html_bold(self):
#         text_node = TextNode("this is bold text", TextType.BOLD)
#         leafnode = Converter.text_node_to_html_node(text_node)
#         self.assertIsInstance(leafnode,LeafNode)
#         self.assertEqual(leafnode._value, "this is bold text")
#         self.assertEqual(leafnode._tag, "b")

#     def test_convert_text_to_html_italics(self):
#         text_node = TextNode("this is italics text", TextType.ITALICS)
#         leafnode = Converter.text_node_to_html_node(text_node)
#         self.assertIsInstance(leafnode,LeafNode)
#         self.assertEqual(leafnode._value, "this is italics text")
#         self.assertEqual(leafnode._tag, "i")
    
#     def test_convert_text_to_html_code(self):
#         text_node = TextNode("this is code text", TextType.CODE)
#         leafnode = Converter.text_node_to_html_node(text_node)
#         self.assertIsInstance(leafnode,LeafNode)
#         self.assertEqual(leafnode._value, "this is code text")
#         self.assertEqual(leafnode._tag, "code")

#     def test_convert_text_to_html_link(self):
#         text_node = TextNode("this is link text", TextType.LINKS, "https://www.someurl.com")
#         leafnode = Converter.text_node_to_html_node(text_node)
#         self.assertIsInstance(leafnode,LeafNode)
#         self.assertEqual(leafnode._value, "this is link text")
#         self.assertEqual(leafnode._tag, "a")
#         self.assertEqual(leafnode._props, {"href":"https://www.someurl.com"})

#     def test_convert_text_to_html_img(self):
#         text_node = TextNode("this is img alt text", TextType.IMAGES, "path/to/img")
#         leafnode = Converter.text_node_to_html_node(text_node)
#         self.assertIsInstance(leafnode,LeafNode)
#         self.assertEqual(leafnode._value, "")
#         self.assertEqual(leafnode._tag, "img")
#         self.assertEqual(leafnode._props, {"src":"path/to/img", "alt": "this is img alt text"})

#     ####################### INELINE MARKDOWN (BOLD, ITALIC, CODE) ###########################

#     def test_delim_bold(self):
#         node = TextNode("This is text with a **bolded** word", TextType.TEXT)
#         new_nodes = Converter.split_nodes_delimiter([node], "**", TextType.BOLD)
#         self.assertListEqual(
#             [
#                 TextNode("This is text with a ", TextType.TEXT),
#                 TextNode("bolded", TextType.BOLD),
#                 TextNode(" word", TextType.TEXT),
#             ],
#             new_nodes,
#         )

#     def test_delim_bold_double(self):
#         node = TextNode(
#             "This is text with a **bolded** word and **another**", TextType.TEXT
#         )
#         new_nodes = Converter.split_nodes_delimiter([node], "**", TextType.BOLD)
#         self.assertListEqual(
#             [
#                 TextNode("This is text with a ", TextType.TEXT),
#                 TextNode("bolded", TextType.BOLD),
#                 TextNode(" word and ", TextType.TEXT),
#                 TextNode("another", TextType.BOLD),
#             ],
#             new_nodes,
#         )

#     def test_delim_bold_multiword(self):
#         node = TextNode(
#             "This is text with a **bolded word** and **another**", TextType.TEXT
#         )
#         new_nodes = Converter.split_nodes_delimiter([node], "**", TextType.BOLD)
#         self.assertListEqual(
#             [
#                 TextNode("This is text with a ", TextType.TEXT),
#                 TextNode("bolded word", TextType.BOLD),
#                 TextNode(" and ", TextType.TEXT),
#                 TextNode("another", TextType.BOLD),
#             ],
#             new_nodes,
#         )

#     def test_delim_italic(self):
#         node = TextNode("This is text with an *italic* word", TextType.TEXT)
#         new_nodes = Converter.split_nodes_delimiter([node], "*", TextType.ITALICS)
#         self.assertListEqual(
#             [
#                 TextNode("This is text with an ", TextType.TEXT),
#                 TextNode("italic", TextType.ITALICS),
#                 TextNode(" word", TextType.TEXT),
#             ],
#             new_nodes,
#         )

#     def test_delim_bold_and_italic(self):
#         node = TextNode("**bold** and *italic*", TextType.TEXT)
#         new_nodes = Converter.split_nodes_delimiter([node], "**", TextType.BOLD)
#         new_nodes = Converter.split_nodes_delimiter(new_nodes, "*", TextType.ITALICS)
#         self.assertListEqual(
#             [
#                 TextNode("bold", TextType.BOLD),
#                 TextNode(" and ", TextType.TEXT),
#                 TextNode("italic", TextType.ITALICS),
#             ],
#             new_nodes,
#         )

#     def test_delim_code(self):
#         node = TextNode("This is text with a `code block` word", TextType.TEXT)
#         new_nodes = Converter.split_nodes_delimiter([node], "`", TextType.CODE)
#         self.assertListEqual(
#             [
#                 TextNode("This is text with a ", TextType.TEXT),
#                 TextNode("code block", TextType.CODE),
#                 TextNode(" word", TextType.TEXT),
#             ],
#             new_nodes,
#         )

#  ####################### INELINE MARKDOWN (IMIAGES, LINKS) ###########################
#     def test_extract_markdown_images(self):
#         matches = Converter.extract_markdown_images(
#             "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
#         )
#         self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

#     def test_extract_markdown_links(self):
#         matches = Converter.extract_markdown_links(
#             "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
#         )
#         self.assertListEqual(
#             [
#                 ("link", "https://boot.dev"),
#                 ("another link", "https://blog.boot.dev"),
#             ],
#             matches,
#         )
    
#     def test_split_nodes_link_empty_node(self):
#         # node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
#         new_nodes = Converter.split_nodes_links([])
#         self.assertListEqual(
#             [],
#             new_nodes,
#         )

#     def test_split_nodes_link(self):
#         node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
#         new_nodes = Converter.split_nodes_links([node])
#         self.assertListEqual(
#             [
#                 TextNode("This is text with a link ", TextType.TEXT),
#                 TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
#                 TextNode(" and ", TextType.TEXT),
#                 TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"),
#             ],
#             new_nodes,
#         )
    
#     def test_split_nodes_img(self):
#         node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
#         new_nodes = Converter.split_nodes_img([node])
#         self.assertListEqual(
#             [
#                 TextNode("This is text with a link ", TextType.TEXT),
#                 TextNode("to boot dev", TextType.IMAGES, "https://www.boot.dev"),
#                 TextNode(" and ", TextType.TEXT),
#                 TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev"),
#             ],
#             new_nodes,
#         )

#     def test_split_image(self):
#         node = TextNode(
#             "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
#             TextType.TEXT,
#         )
#         new_nodes = Converter.split_nodes_img([node])
#         self.assertListEqual(
#             [
#                 TextNode("This is text with an ", TextType.TEXT),
#                 TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
#             ],
#             new_nodes,
#         )

#     def test_split_image_single(self):
#         node = TextNode(
#             "![image](https://www.example.COM/IMAGE.PNG)",
#             TextType.TEXT,
#         )
#         new_nodes = Converter.split_nodes_img([node])
#         self.assertListEqual(
#             [
#                 TextNode("image", TextType.IMAGES, "https://www.example.COM/IMAGE.PNG"),
#             ],
#             new_nodes,
#         )

#     def test_split_images(self):
#         node = TextNode(
#             "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
#             TextType.TEXT,
#         )
#         new_nodes = Converter.split_nodes_img([node])
#         self.assertListEqual(
#             [
#                 TextNode("This is text with an ", TextType.TEXT),
#                 TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
#                 TextNode(" and another ", TextType.TEXT),
#                 TextNode("second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"),
#             ],
#             new_nodes,
#         )

#     def test_split_links(self):
#         node = TextNode(
#             "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
#             TextType.TEXT,
#         )
#         new_nodes = Converter.split_nodes_links([node])
#         self.assertListEqual(
#             [
#                 TextNode("This is text with a ", TextType.TEXT),
#                 TextNode("link", TextType.LINKS, "https://boot.dev"),
#                 TextNode(" and ", TextType.TEXT),
#                 TextNode("another link", TextType.LINKS, "https://blog.boot.dev"),
#                 TextNode(" with text that follows", TextType.TEXT),
#             ],
#             new_nodes,
#         )

#     def test_bold_italic_code_image_link(self):
#         text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
#         node_list = Converter.text_to_textnodes(text)
#         self.assertListEqual(
#             [
#                 TextNode("This is ", TextType.TEXT),
#                 TextNode("text", TextType.BOLD),
#                 TextNode(" with an ", TextType.TEXT),
#                 TextNode("italic", TextType.ITALICS),
#                 TextNode(" word and a ", TextType.TEXT),
#                 TextNode("code block", TextType.CODE),
#                 TextNode(" and an ", TextType.TEXT),
#                 TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
#                 TextNode(" and a ", TextType.TEXT),
#                 TextNode("link", TextType.LINKS, "https://boot.dev"),
#             ],
#             node_list,
#         )
    
#     def test_code_italic_bold_Image_link(self):
#         text = "This is `text in code` *italic words* and **some bold text** with an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
#         node_list = Converter.text_to_textnodes(text)
#         self.assertListEqual(
#             [
#                 TextNode("This is ", TextType.TEXT),
#                 TextNode("text in code", TextType.CODE),
#                 TextNode(" ", TextType.TEXT),
#                 TextNode("italic words", TextType.ITALICS),
#                 TextNode(" and ", TextType.TEXT),
#                 TextNode("some bold text", TextType.BOLD),
#                 TextNode(" with an ", TextType.TEXT),
#                 TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
#                 TextNode(" and a ", TextType.TEXT),
#                 TextNode("link", TextType.LINKS, "https://boot.dev"),
#             ],
#             node_list,
#         )
    
#     def test_Image_code_italic_bold_link(self):
#         text = "an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) with `text in code` *italic words* and **some bold text** with a [link](https://boot.dev) and text at the end"
#         node_list = Converter.text_to_textnodes(text)
#         self.assertListEqual(
#             [
#                 TextNode("an ", TextType.TEXT),
#                 TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
#                 TextNode(" with ", TextType.TEXT),
#                 TextNode("text in code", TextType.CODE),
#                 TextNode(" ", TextType.TEXT),
#                 TextNode("italic words", TextType.ITALICS),
#                 TextNode(" and ", TextType.TEXT),
#                 TextNode("some bold text", TextType.BOLD),
#                 TextNode(" with a ", TextType.TEXT),
#                 TextNode("link", TextType.LINKS, "https://boot.dev"),
#                 TextNode(" and text at the end", TextType.TEXT),
#             ],
#             node_list,
#         )

#     def test_Image_and_link(self):
#         text = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) [link](https://boot.dev)"
#         node_list = Converter.text_to_textnodes(text)
#         self.assertListEqual(
#             [
#                 TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
#                 TextNode(" ", TextType.TEXT),
#                 TextNode("link", TextType.LINKS, "https://boot.dev"),
#             ],
#             node_list,
#         )

#     def test_markdown_to_blocks(self):
#         text = '''
# # This is a heading

# This is a paragraph of text. It has some **bold** and *italic* words inside of it.

# * This is the first list item in a list block
# * This is a list item
# * This is another list item
# '''
#         result = Converter.markdown_to_blocks(text)
#         self.assertListEqual(
#             [
#                 '# This is a heading', 
#                 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
#                 '* This is the first list item in a list block\n* This is a list item\n* This is another list item',
#             ],
#             result,
#         )
    
#     def test_markdown_to_blocks_newlines(self):
#         md = """
# This is **bolded** paragraph




# This is another paragraph with *italic* text and `code` here
# This is the same paragraph on a new line

# * This is a list
# * with items
# """
#         blocks = Converter.markdown_to_blocks(md)
#         self.assertEqual(
#             blocks,
#             [
#                 "This is **bolded** paragraph",
#                 "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
#                 "* This is a list\n* with items",
#             ],
#         )

#     def test_block_to_block_types(self):
#         block = "# heading"
#         self.assertEqual(Converter.block_to_blocktype(block), BlockType.HEADING)
#         block = "```\ncode\n```"
#         self.assertEqual(Converter.block_to_blocktype(block), BlockType.CODE)
#         block = "> quote\n> more quote"
#         self.assertEqual(Converter.block_to_blocktype(block), BlockType.QUOTE)
#         block = "* list\n* items"
#         self.assertEqual(Converter.block_to_blocktype(block), BlockType.U_LIST)
#         block = "1. list\n2. items"
#         self.assertEqual(Converter.block_to_blocktype(block), BlockType.O_LIST)
#         block = "paragraph"
#         self.assertEqual(Converter.block_to_blocktype(block), BlockType.PARAGRAPH)

############################### Test Full Markdown BLocks ###########################################

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = Converter.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = Converter.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = Converter.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = Converter.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = Converter.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_full_markdown(self):
        markdown = """
# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

> All that is gold does not glitter

## Reasons I like Tolkien

* You can spend years studying the legendarium and still not understand its depths
* It can be enjoyed by children and adults alike
* Disney *didn't ruin it*
* It created an entirely new genre of fantasy

## My favorite characters (in order)

1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn

Here's what `elflang` looks like (the perfect coding language):

```
func main(){
    fmt.Println("Hello, World!")
}
```
"""
        node = Converter.markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Tolkien Fan Club</h1><p><b>I like Tolkien</b>. Read my <a href='/majesty>first post here</a> (sorry the link doesn't work yet)<blockquote>All that is gold does not glitter</blockquote><h2>Reasons I like Tolkien</h2>"
        )
        

if __name__ == "__main__":
    unittest.main()
