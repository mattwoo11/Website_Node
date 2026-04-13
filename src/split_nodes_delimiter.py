from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
        elif delimiter not in node.text:
            new_list.append(node)
        else:
            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                if not part:
                    continue
                if i % 2 == 0:
                    new_list.append(TextNode(part, TextType.TEXT))
                else:
                    new_list.append(TextNode(part, text_type))
    return new_list