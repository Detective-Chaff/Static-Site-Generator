import os
import shutil
from converter import Converter

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
                shutil.copy(path, os.path.join(dest_dir, item))
            else:
                copy_recursive(path)

    return copy_recursive(src_dir)

def extract_title(markdown):
    lines = markdown.split("\n\n")
    title = ""
    found = False
    for line in lines:
        if line.startswith("# "):
            title = line[2:].lstrip().rstrip()
            found = True
            break
    if not found:
        raise Exception("no valid title found.")
    return title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from: {from_path} to {dest_path} using {template_path}")
    if os.path.exists(from_path):
        markdown = None
        template = None

        # markdown file
        with open(from_path) as md_file:
            markdown = md_file.read()

        # template file
        with open(template_path) as temp_file:
            template = temp_file.read()
        
            # Get Title
            title = extract_title(markdown)
            node = Converter.markdown_to_html_node(markdown)
            html = node.to_html()
            # Inject Title
            title_replace = template.replace("{{ Title }}", title)

            # Inject Content
            final = title_replace.replace("{{ Content }}", html)
        
        dest = os.path.dirname(dest_path)
        os.makedirs(dest, exist_ok= True)
        with open(dest_path, "w") as wf:
            wf.write(final)


def generate_pages_recursive(from_path, template_path, dest_path):
    if not os.path.exists(from_path):
        return
    markdown = None
    template = None
    source = os.listdir(from_path)
    if not os.path.exists(dest_path):               
        print(f"creating dir: {dest_path}")
        print("dir created...")
        os.mkdir(dest_path)
    for item in source:
        dest = dest_path
        path = os.path.join(from_path, item)
        if os.path.isfile(path):
            dest = os.path.join(dest, item).replace("md", "html")
            with open(path) as md_file:
                markdown = md_file.read()
            
            with open(template_path) as temp_file:
                template = temp_file.read()
        
            title = extract_title(markdown)
            node = Converter.markdown_to_html_node(markdown)
            html = node.to_html()
            title_replace = template.replace("{{ Title }}", title)
            final = title_replace.replace("{{ Content }}", html)

            with open(dest, "w") as wf:
                wf.write(final) 
        else:
            dest = os.path.join(dest_path, item)
            generate_pages_recursive(path, template_path, dest)

