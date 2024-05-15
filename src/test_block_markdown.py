import unittest

from block_markdown import (
  markdown_to_blocks
)

class TestBlockMarkdown(unittest.TestCase):
  def test_markdown_to_blocks(self):
    string = markdown_to_blocks("")
    block = ""
    self.assertEqual(string, block)
    