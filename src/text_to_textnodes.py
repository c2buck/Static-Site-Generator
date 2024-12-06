from textnode import TextType
from textnode import TextNode
from extract_links import extract_markdown_images
from extract_links import extract_markdown_links
from split_delimiter import split_nodes_delimiter

def text_to_textnodes(text):
    # Start with a single TextNode for the entire input text
    nodes = [TextNode(text, TextType.TEXT)]

    # Process nodes to extract images
    new_nodes = []
    for node in nodes:
        if node.text_type == TextType.TEXT:
            new_nodes.extend(extract_markdown_images(node.text))
        else:
            new_nodes.append(node)
    nodes = new_nodes

    # Process nodes to extract links
    new_nodes = []
    for node in nodes:
        if node.text_type == TextType.TEXT:
            new_nodes.extend(extract_markdown_links(node.text))
        else:
            new_nodes.append(node)
    nodes = new_nodes

    # Process nodes to extract bold text
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    # Process nodes to extract italic text
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    # Process nodes to extract code text
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes
