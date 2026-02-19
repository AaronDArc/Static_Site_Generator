from textnode import TextNode

class HTMLNode():
    def __init__(self,tag=None,text=None,htmlnode_objects=None,key_pairs=None):
        self.tag = tag # Without tag will render as text
        self.value = text # Without value will assume children
        self.children = htmlnode_objects # without children assume value
        self.props = key_pairs # Won't have any attributes

    def to_html(self):
        raise NotImplementedError()
        # Will be overridden with child classes


    def props_to_html(self):
        if not self.props:
            return ""
        # Goal -> href="https://www.google.com" target="_blank"
        return "".join(f' {key}="{item}"' for key,item in self.props.items())
    
    def __repr__(self):
        print(self.value)
        print(self.tag)
        print(self.children)
        print(self.props.items())

    