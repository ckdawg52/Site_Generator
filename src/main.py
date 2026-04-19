from textnode import TextType, TextNode
from blocks import markdown_to_blocks, BlockType, block_to_block_type
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from conversion import text_to_textnodes, text_node_to_html_node
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from extract import extract_markdown_images, extract_markdown_links, extract_title
from markdown_to_html import markdown_to_html_node
import os
import shutil

def copy_static_to_public(source, destination):
    if not os.path.exists(source):
        raise ValueError(f"Source directory {source} does not exist")
    if not os.path.exists(destination):
        os.makedirs(destination)
    shutil.rmtree(destination)
    recursive_copy_helper(source, destination)


def recursive_copy_helper(source, destination):
    if not os.path.exists(source):
        raise ValueError(f"Source directory {source} does not exist")
    if not os.path.exists(destination):
        os.makedirs(destination)
    if os.path.isfile(source):
        shutil.copy(source, destination)
        return
    dir_list = os.listdir(source)
    for item in dir_list:
        if os.path.isfile(item):
            shutil.copy(os.path.join(source, item), os.path.join(destination, item))
        else:
            recursive_copy_helper(os.path.join(source, item), os.path.join(destination, item))

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    fp_contents = open(from_path).read()
    temp_contents = open(template_path).read()
    node = markdown_to_html_node(fp_contents)
    title = extract_title(fp_contents)
    temp_contents = temp_contents.replace("{{ Title }}", title, 1)
    temp_contents = temp_contents.replace("{{ Content }}", node.to_html(), 1)
    directory = os.path.dirname(dest_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    open(dest_path, mode="w").write(temp_contents)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    for content in contents:
        if os.path.isdir(os.path.join(dir_path_content, content)):
            generate_page_recursive(os.path.join(dir_path_content, content), template_path, os.path.join(dest_dir_path, content))
        else:
            if not content.endswith(".md"):
                continue
            new_content = content[:-3] + ".html"
            generate_page(os.path.join(dir_path_content, content), template_path, os.path.join(dest_dir_path, new_content))


def main():
    copy_static_to_public("static", "public")
    generate_page_recursive("content", "template.html", "public")


main()