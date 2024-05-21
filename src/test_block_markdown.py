import unittest

from block_markdown import (
  markdown_to_blocks,
  block_to_block_type,
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


  def test_block_to_block_type_heading(self):
    block = "## This is a heading"
    self.assertEqual(block_to_block_type(block), block_type_heading)
  
  
  def test_block_to_block_type_code(self):
    block = "```\ncode block\n```"
    self.assertEqual(block_to_block_type(block), block_type_code)
    
    
  def test_block_to_block_type_quote(self):
    block = "> This is a quote\n> and another quote"
    self.assertEqual(block_to_block_type(block), block_type_quote)
    
    
  def test_block_to_block_type_uolist(self):
    block = "* This is a list element\n* more stuff"
    self.assertEqual(block_to_block_type(block), block_type_unordered_list)
    
    
  def test_block_to_block_type_uolist2(self):
    block = "- This is a list element\n- and another list element"
    self.assertEqual(block_to_block_type(block), block_type_unordered_list)
    
    
  def test_block_to_block_olist(self):
    block = "1. This is an ordered list\n2. Good luck have fun"
    self.assertEqual(block_to_block_type(block), block_type_ordered_list)
    
    
  def test_block_to_block_paragraph(self):
    block = "This is a paragraph"
    self.assertEqual(block_to_block_type(block), block_type_paragraph)

if __name__ == '__main__':
  unittest.main()