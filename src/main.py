import os
import shutil
from converter import Converter
from textnode import TextNode, TextType


def copy_to_public(src_dir):
    dest = src_dir.replace("./static", "./public")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)

    def copy_recursive(src_dir):
        if not os.path.exists(src_dir):
            return
        source = os.listdir(src_dir)
        dest_dir = src_dir.replace("./static", "./public") 
        if not os.path.exists(dest_dir):               
            print(f"creating dir: {dest_dir}")
            print("dir created...")
            os.mkdir(dest_dir)
        for item in source:
            path = os.path.join(src_dir, item)
            if os.path.isfile(path):
                print(f"copying file: {path} to: {os.path.join(dest_dir, item)}")
                new_file = shutil.copy(path, os.path.join(dest_dir, item))
            else:
                copy_recursive(path)

    return copy_recursive(src_dir)

def main():
    copy_to_public("./static")

if __name__ == "__main__":
    main()

