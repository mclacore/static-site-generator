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