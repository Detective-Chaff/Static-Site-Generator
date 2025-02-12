from src.htmlnode import HTMLnode

class ParentNode(HTMLnode):

    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self._tag is None or len(self._tag) == 0:
            return ValueError("'Tag' must contain a value")
        
        if self._children is None:
            return ValueError("'children' cannot be empty")

        html_str = f'<{self._tag}{self.props_to_html()}>'
        for child in self._children:
            html_str += child.to_html()
        html_str += f'</{self._tag}>'
        return html_str
        