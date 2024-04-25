import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "bold")
    self.assertEqual(node, node2)


  def test_url(self):
    node = TextNode("This is a none url", "bold", None)
    self.assertIsNone(node.url)


  def test_not_eq(self):
    node = TextNode("This is a text node", "bold")
    node2 = TextNode("This is not a text node", "bold")
    self.assertNotEqual(node, node2)


  def test_text_type(self):
    node = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "italic")
    self.assertNotEqual(node, node2)


if __name__ == "__main__":
  unittest.main()