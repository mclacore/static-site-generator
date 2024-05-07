from textnode import (
  TextNode,
  text_type_text,
  text_type_bold,
  text_type_italic,
  text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != text_type_text:
      new_nodes.append(old_node)
      continue
    split_nodes = []
    elements = old_node.text.split(delimiter)
    if len(elements) % 2 == 0:
      raise Exception("Invalid markdown, element not closed")
    for i in range(len(elements)):
      if elements[i] == "":
        continue
      if i % 2 == 0:
        split_nodes.append(TextNode(elements[i], text_type_text))
      else:
        split_nodes.append(TextNode(elements[i], text_type))
    new_nodes.extend(split_nodes)

  return new_nodes