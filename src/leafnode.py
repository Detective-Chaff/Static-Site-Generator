
from htmlnode import HTMLnode

class LeafNode(HTMLnode):
    # constructor
    def __init__(self, tag, value, props = None,):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self._value is None or len(self._value) == 0:
            raise ValueError("'Value' must not be empty")
        
        if self._tag is None or len(self._tag) == 0:
            return f"{self._value}"
        
        return f"<{self._tag}{self.props_to_html()}>{self._value}</{self._tag}>"
