import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

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