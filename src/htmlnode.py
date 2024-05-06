class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
    
  def to_html(self):
    raise NotImplementedError("to_html method not implemented")
  
  def props_to_html(self):
    if self.props is None:
      return ""
    props_html = ""
    for key, value in self.props.items():
      props_html += f' {key}="{value}"'
    return props_html
      
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None, props)

  def to_html(self):
    if self.value is None:
      raise ValueError("LeafNode must have a value")
    if self.tag is None:
      return self.value
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
  
  def __repr__(self):
    return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag == "":
      raise ValueError("Tag cannot be an empty string")
    if self.tag is None:
      raise ValueError("ParentNode requires a tag")
    if not self.children:
      raise ValueError("ParentNode requires at least 1 child")
    
    html_output = f"<{self.tag}"
    
    if self.props is not None:
      props_html = self.props_to_html()
      html_output += props_html
    html_output += ">"
    
    for child in self.children:
      child_html = child.to_html()
      html_output += child_html
      
    html_output += f"</{self.tag}>"
    
    return html_output
