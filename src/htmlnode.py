class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if self.props:
            for key in self.props:
                result += f' {key}="{self.props[key]}"'
        return result
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value,  props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if  self.value == None:
            raise ValueError
        elif self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("The object has no tag")
        elif self.children == None:
            raise ValueError("Children has no value.")
        else:
            result = ""
            for x in self.children:
                result += x.to_html()
            return f"<{self.tag}>{result}</{self.tag}>"