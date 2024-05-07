import unittest

from extract_markdown import (
  extract_markdown_links,
  extract_markdown_images
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