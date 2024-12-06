import re
from textnode import TextNode, TextType


def extract_markdown_images(old_nodes):
    new_nodes = []
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

     # If the input is a string, convert it to a list with one TextNode
    if isinstance(old_nodes, str):
        nodes = [TextNode(old_nodes, TextType.TEXT)]
    else:
        nodes = old_nodes

    for node in nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        matches = re.finditer(pattern, node.text)
        current_index = 0

        for match in matches:
            if match.start() > current_index:
                text_before = node.text[current_index:match.start()]  # This is correct!
                new_nodes.append(TextNode(text_before, TextType.TEXT))
            
            # Add the image node
            alt_text = match.group(1)
            url = match.group(2)
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            
            current_index = match.end()

        if current_index < len(node.text):
            text_after = node.text[current_index:]  # Just get everything from current_index to the end
            new_nodes.append(TextNode(text_after, TextType.TEXT))

        
        

    return new_nodes

   


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if not images:
            result.append(node)
            continue

        for alt_text, image_url in images:
            sections = node.text.split(f"![{alt_text}]({image_url})", 1)

              # If there's text before the link, create a TEXT node
            if sections[0]:
                result.append(TextNode(sections[0], TextType.TEXT))
            
            # Create and append the link node
            result.append(TextNode(alt_text, TextType.IMG, image_url))
            
            # If there's text after the link, create a TEXT node
            if sections[1]:
                result.append(TextNode(sections[1], TextType.TEXT))
    
    return result


def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if not links:
            result.append(node)
            continue

        for link_text, link_url in links:
            sections = node.text.split(f"[{link_text}]({link_url})", 1)

              # If there's text before the link, create a TEXT node
            if sections[0]:
                result.append(TextNode(sections[0], TextType.TEXT))
            
            # Create and append the link node
            result.append(TextNode(link_text, TextType.LINK, link_url))
            
            # If there's text after the link, create a TEXT node
            if sections[1]:
                result.append(TextNode(sections[1], TextType.TEXT))
    
    return result