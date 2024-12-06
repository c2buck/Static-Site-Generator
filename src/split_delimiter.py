from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        parts = node.text.split(delimiter)
        for i, part in enumerate(parts):
            # If i is even (0, 2, 4...) it's outside delimiters
            # If i is odd (1, 3, 5...) it's between delimiters
            current_type = TextType.TEXT if i % 2 == 0 else text_type
            if part != "":  # Only add non-empty parts
                new_nodes.append(TextNode(part, current_type))

    return new_nodes




