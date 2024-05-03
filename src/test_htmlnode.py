import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
  def test_props_to_html(self):
    node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")


class testLeafNode(unittest.TestCase):
  def test_no_props(self):
    node = LeafNode("p", "This is a paragraph of text.")
    self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
    
  def test_with_props(self):
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")


class testParentNode(unittest.TestCase):
  def test_simple_html(self):
    child_node = LeafNode("b", "This is bold text")
    parent_node = ParentNode("p", [child_node])
    self.assertEqual(parent_node.to_html(), "<p><b>This is bold text</b></p>")
    
  def test_nested_parents(self):
    header_node = LeafNode("h1", "Welcome to my page")
    paragraph1_node = LeafNode("p", "This is my first paragraph")
    bold_text_node = LeafNode("em", " very important")
    paragraph2_node = ParentNode("p", [LeafNode(None, "This part is"), bold_text_node, LeafNode(None, ".")])
    selection_node = ParentNode("div", [header_node, paragraph1_node, paragraph2_node])
    self.assertEqual(selection_node.to_html(), "<div><h1>Welcome to my page</h1><p>This is my first paragraph</p><p>This part is<em> very important</em>.</p></div>")

  def test_no_tag(self):
    child_node = LeafNode(None, "Plain text")
    with self.assertRaises(ValueError):
      parent_node = ParentNode(None, [child_node])
      parent_node.to_html()

  def test_no_children(self):
    with self.assertRaises(ValueError):
      parent_node = ParentNode("p", [])
      parent_node.to_html()

  def test_with_props(self):
    props = {"foo": "bar", "austin": "powers"}
    child_node = LeafNode("b", "This is bold text")
    parent_node = ParentNode("p", [child_node], props=props)
    self.assertEqual(parent_node.to_html(), '<p foo="bar" austin="powers"><b>This is bold text</b></p>', "HTML output with props did not match expected output.")
    
  def test_empty_string_as_tag(self):
    child_node = LeafNode("b", "This is bold text")
    with self.assertRaises(ValueError):
      parent_node = ParentNode("", [child_node])
      parent_node.to_html()
