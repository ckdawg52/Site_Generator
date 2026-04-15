from textnode import TextNode, TextType
from extract import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if len(node.text.split(delimiter)) % 2 == 0:
            raise Exception(f"Missing either opening or closing {delimiter} delimeter")
        splits = node.text.split(delimiter)
        for i in range(0, len(splits)):
            if i % 2 == 0:
                if splits[i] != "":
                    new_nodes.append(TextNode(splits[i], TextType.TEXT))
            else:
                if splits[i] != "":
                    new_nodes.append(TextNode(splits[i], text_type))
    return new_nodes
        
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if extract_markdown_images(node.text) == []:
            new_nodes.append(TextNode(node.text, TextType.TEXT))
            continue
        images = extract_markdown_images(node.text)
        text = node.text
        for image in images:
            split = text.split(f"![{image[0]}]({image[1]})", 1)
            text = split[1]
            new_nodes.append(TextNode(split[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if extract_markdown_links(node.text) == []:
            new_nodes.append(TextNode(node.text, TextType.TEXT))
            continue
        links = extract_markdown_links(node.text)
        text = node.text
        for link in links:
            split = text.split(f"[{link[0]}]({link[1]})", 1)
            text = split[1]
            new_nodes.append(TextNode(split[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

