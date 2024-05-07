import re


def extract_markdown_images(text):
  tuple = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
  return tuple


def extract_markdown_links(text):
  tuple = re.findall(r"\[(.*?)\]\((.*?)\)", text)
  return tuple
