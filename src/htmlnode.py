

class HTMLnode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self._tag = tag # html tag
        self._value = value # content contained in the tag
        self._children = children # List of HTMLnode objects as children of this HTMLnode
        self._props = props # properties of the tag i.e class, href, id, etc
    
# Getters and Setters
    #tag
    def get_tag(self):
        return self._tag
    def set_tag(self, tag):
        self._tag = tag

    #value
    def get_value(self):
        return self._value
    def set_value(self, value):
        self._value = value
    
    # children
    def get_children(self):
        return self._children
    def set_children(self, children):
        self._children = children

    #props
    def get_props(self):
        return self._props
    def set_props(self, props):
        self._props = props

# class methods
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self._props is None:
            return ""
        props_html = ""
        for k, v in self.get_props().items():
            props_html += f' {k}="{v}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLnode(tag: {self._tag}, value: {self._value}, children: {self._children}, props: {self._props})"