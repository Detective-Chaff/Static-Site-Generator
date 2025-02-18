from converter import Converter
# from parser import Parser
from textnode import TextNode, TextType


def main():
    # node = TextNode("this is a text node", "bold", "https://www.boot.dev")
    # print(node)
    # print("hello world")
    node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)

    Converter.extract_markdown_images(node.text)

        

if __name__ == "__main__":
    main()

