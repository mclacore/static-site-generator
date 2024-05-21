import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
  result = []
  blocks = markdown.split("\n\n")
  for block in blocks:
    if block == "":
      continue
    block = block.strip()
    result.append(block)
  return result


def block_to_block_type(block):
  lines = block.split("\n")
  
  if (
    block.startswith("#") or
    block.startswith("##") or
    block.startswith("###") or
    block.startswith("####") or
    block.startswith("#####") or
    block.startswith("######")
  ):
    return block_type_heading
  if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
    return block_type_code
  if block.startswith(">"):
    for line in lines:
      if not line.startswith(">"):
        return block_type_paragraph
    return block_type_quote
  if block.startswith("* "):
    for line in lines:
      if not line.startswith("* "):
        return block_type_paragraph
    return block_type_unordered_list
  if block.startswith("- "):
    for line in lines:
      if not line.startswith("- "):
        return block_type_paragraph
    return block_type_unordered_list
  if re.match(r'^\d+\.\s', block):
    for line in lines:
      if not re.match(r'^\d+\.\s', line):
        return block_type_paragraph
    return block_type_ordered_list
  return block_type_paragraph