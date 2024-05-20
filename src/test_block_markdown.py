import unittest

from block_markdown import (
  markdown_to_blocks,
  block_type_paragraph,
  block_type_code,
  block_type_heading,
  block_type_ordered_list,
  block_type_quote,
  block_type_unordered_list,
)

class TestBlockMarkdown(unittest.TestCase):
  def test_markdown_to_blocks(self):
    markdown = """
This is a **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
    expected_blocks = [
      "This is a **bolded** paragraph",
      "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
      "* This is a list\n* with items"
    ]
    
    result_blocks = markdown_to_blocks(markdown)
    self.assertEqual(result_blocks, expected_blocks)


  def test_markdown_to_blocks_morelines(self):
    markdown = """
This is a **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
    expected_blocks = [
      "This is a **bolded** paragraph",
      "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
      "* This is a list\n* with items"
    ]
    result_blocks = markdown_to_blocks(markdown)
    self.assertEqual(result_blocks, expected_blocks)

if __name__ == '__main__':
  unittest.main()