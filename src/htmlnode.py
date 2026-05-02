

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #string
        self.value = value #string
        self.children = children # list of HTMLNode objects
        self.props = props #dictionary of {string:string}

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        attributes = ""
        if not self.props:
            return attributes
        
        for prop_key in self.props:
            attributes += f" {prop_key}=\"{self.props[prop_key]}\""

        return attributes
    
    def __repr__(self):
        rep = "HTMLNode:\n"
        rep += f"tag={self.tag}\n"
        rep += f"value={self.value}\n"
        rep += f"children={self.children}\n"
        rep += f"props={self.props}\n"

        return rep