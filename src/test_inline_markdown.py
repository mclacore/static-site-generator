import unittest

from inline_markdown import (
  split_nodes_delimiter,
  extract_markdown_images,
  extract_markdown_links,
  split_nodes_image,
  split_nodes_link,
  text_to_textnodes,
)

from textnode import (
  TextNode,
  text_type_text,
  text_type_bold,
  text_type_italic,
  text_type_code,
  text_type_link,
  text_type_image,
)

class TestInlineMarkdown(unittest.TestCase):
  def test_bold(self):
    node = TextNode("This is a text with a **bolded** word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    self.assertListEqual(
      [
        TextNode("This is a text with a ", text_type_text),
        TextNode("bolded", text_type_bold),
        TextNode(" word", text_type_text),
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
        TextNode("another", text_type_bold),
      ],
      new_nodes
    )
    
  def test_extract_markdown_images(self):
    matches = extract_markdown_images("This is text with an ![image](https://imgur.com/image.png)")
    self.assertListEqual([("image", "https://imgur.com/image.png")], matches)
    
  def test_extract_markdown_links(self):
    matches = extract_markdown_links("This is text with a [link](https://google.com) and [another link](https://maps.google.com)")
    self.assertListEqual([
      ("link", "https://google.com"),
      ("another link", "https://maps.google.com"),
    ], matches)
    
  def test_split_image(self):
    node = TextNode("This is text with an ![image](https://imgur.com/image.png)", text_type_text)
    new_nodes = split_nodes_image([node])
    self.assertListEqual([
      TextNode("This is text with an ", text_type_text),
      TextNode("image", text_type_image, "https://imgur.com/image.png"),
    ], new_nodes)
    
  def test_split_image_single(self):
    node = TextNode("![image](https://imgur.com/image.png)", text_type_text)
    new_nodes = split_nodes_image([node])
    self.assertListEqual([
      TextNode("image", text_type_image, "https://imgur.com/image.png"),
    ], new_nodes)
    
  def test_split_images(self):
    node = TextNode(
      "This is text with an ![image](https://imgur.com/image.png) and another ![image2](https://imgur.com/image2.png)", text_type_text
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual([
      TextNode("This is text with an ", text_type_text),
      TextNode("image", text_type_image, "https://imgur.com/image.png"),
      TextNode(" and another ", text_type_text),
      TextNode("image2", text_type_image, "https://imgur.com/image2.png"),
    ], new_nodes)
    
  def test_split_links(self):
    node = TextNode(
      "This is test with a [link](https://google.com) and [another link](https://maps.google.com) with text after it", text_type_text
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual([
      TextNode("This is test with a ", text_type_text),
      TextNode("link", text_type_link, "https://google.com"),
      TextNode(" and ", text_type_text),
      TextNode("another link", text_type_link, "https://maps.google.com"),
      TextNode(" with text after it", text_type_text),
    ], new_nodes)
    
  def test_text_to_textnodes(self):
    text = text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![image](https://imgur.com/image.png) and a [link](https://google.com)")
    self.assertListEqual([
      TextNode("This is ", text_type_text),
      TextNode("text", text_type_bold),
      TextNode(" with an ", text_type_text),
      TextNode("italic", text_type_italic),
      TextNode(" word and a ", text_type_text),
      TextNode("code block", text_type_code),
      TextNode(" and an ", text_type_text),
      TextNode("image", text_type_image, "https://imgur.com/image.png"),
      TextNode(" and a ", text_type_text),
      TextNode("link", text_type_link, "https://google.com"),
      ], text)

if __name__ == "__main__":
  unittest.main()