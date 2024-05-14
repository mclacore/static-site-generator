import re

from textnode import (
  TextNode,
  text_type_text,
  text_type_bold,
  text_type_italic,
  text_type_code,
  text_type_image,
  text_type_link
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


def extract_markdown_images(text):
  match = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
  return match


def extract_markdown_links(text):
  match = re.findall(r"\[(.*?)\]\((.*?)\)", text)
  return match


def split_nodes_image(old_nodes):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != text_type_text:
      new_nodes.append(old_node)
      continue
    original_text = old_node.text
    image_tup = extract_markdown_images(original_text)
    if len(image_tup) == 0:
      new_nodes.append(old_node)
      continue
    for image in image_tup:
      elements = original_text.split(f"![{image[0]}]({image[1]})", 1)
      if len(elements) != 2:
        raise ValueError("Invalid markdown, element not closed")
      if elements[0] != "":
        new_nodes.append(TextNode(elements[0], text_type_text))
      new_nodes.append(
        TextNode(
          image[0],
          text_type_image,
          image[1]
        )
      )
      original_text = elements[1]
    if original_text != "":
      new_nodes.append(TextNode(original_text, text_type_text))

  return new_nodes

def split_nodes_link(old_nodes):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != text_type_text:
      new_nodes.append(old_node)
      continue
    original_text = old_node.text
    link_tup = extract_markdown_links(original_text)
    if len(link_tup) == 0:
      new_nodes.append(old_node)
      continue
    for link in link_tup:
      elements = original_text.split(f"[{link[0]}]({link[1]})", 1)
      if len(elements) != 2:
        raise ValueError("Invalid markdown, element not closed")
      if elements[0] != "":
        new_nodes.append(TextNode(elements[0], text_type_text))
      new_nodes.append(TextNode(link[0], text_type_link, link[1]))
      original_text = elements[1]
    if original_text != "":
      new_nodes.append(TextNode(original_text, text_type_text))

  return new_nodes
