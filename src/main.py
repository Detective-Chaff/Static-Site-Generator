from staticcopy import copy_to_public, generate_page, generate_pages_recursive



def main():
    copy_to_public("./static")
    generate_pages_recursive("./content", "./template.html", "./public")

if __name__ == "__main__":
    main()

