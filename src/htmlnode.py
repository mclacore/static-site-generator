class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = [] if children is None else children
    self.props = {} if props is None else props
    
  def to_html(self):
    raise NotImplementedError
  
  def props_to_html(self):
    all_kv = []
    for k, v in self.props.items():
      all_kv.append(f'{k}="{v}"')  
    return " ".join(all_kv)
  
  def __repr__(self):
    return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"