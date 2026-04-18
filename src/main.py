from textnode import TextType, TextNode
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

def main():
    copy_static_to_public("static", "public")


main()