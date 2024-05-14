import unittest

from inline_markdown import (
  split_nodes_delimiter,
  extract_markdown_images,
  extract_markdown_links
)

from textnode import (
  TextNode,
  text_type_text,
  text_type_bold,
  text_type_italic,
  text_type_code,
)

class TestInlineMarkdown(unittest.TestCase):
  def test_bold(self):
    node = TextNode("This is a text with a **bolded** word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    self.assertListEqual(
      [
        TextNode("This is a text with a ", text_type_text),
        TextNode("bolded", text_type_bold),
        TextNode(" word", text_type_text)
      ],
      new_nodes
    )


class TestExtractMarkdown(unittest.TestCase):
  def test_extract_link(self):
    text = "This is a text with a [link](https://google.com) and [another](https://boot.dev)"
    extracted = [
      ("link", "https://google.com"),
      ("another", "https://boot.dev")
    ]
    self.assertListEqual(extract_markdown_links(text), extracted)
    
  def test_extract_image(self):
    text = "This is a text with an ![image](https://imgur.com/foo/bar.png)"
    extracted = [
      ("image", "https://imgur.com/foo/bar.png")
    ]
    self.assertListEqual(extract_markdown_images(text), extracted)
    
  def test_bold_double(self):
    node = TextNode("This is a text with a **bolded** word and **another**", text_type_text)
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    self.assertListEqual(
      [
        TextNode("This is a text with a ", text_type_text),
        TextNode("bolded", text_type_bold),
        TextNode(" word and ", text_type_text),
        TextNode("another", text_type_bold)
      ],
      new_nodes
    )


if __name__ == "__main__":
  unittest.main()