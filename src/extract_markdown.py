import re
from textnode import *
from split_nodes_delimiter import *

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_list = []
    for node in old_nodes:
        original_text = node.text
        if node.text_type != TextType.TEXT:
            new_list.append(node)
        else:
            images = extract_markdown_images(node.text)
            if not images:
                continue
            else:
                for x in images:
                    sections = original_text.split(f"![{x[0]}]({x[1]})", 1)
                    if sections[0] != "":
                        new_list.append(TextNode(sections[0], TextType.TEXT))

                    new_list.append(TextNode(x[0], TextType.IMAGE, x[1]))
                    original_text = sections[1]
                if original_text != "":
                    new_list.append(TextNode(original_text, TextType.TEXT))
    return new_list

def split_nodes_link(old_nodes):
    new_list = []
    for node in old_nodes:
        original_text = node.text
        if node.text_type != TextType.TEXT:
            new_list.append(node)
        else:
            links = extract_markdown_links(node.text)
            if not links:
                continue
            else:
                for x in links:
                    sections = original_text.split(f"[{x[0]}]({x[1]})", 1)
                    if sections[0] != "":
                        new_list.append(TextNode(sections[0], TextType.TEXT))

                    new_list.append(TextNode(x[0], TextType.LINK, x[1]))
                    original_text = sections[1]
                if original_text != "":
                    new_list.append(TextNode(original_text, TextType.TEXT))
    return new_list

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)