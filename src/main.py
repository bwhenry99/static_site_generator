import copytopublic
import generatepage

def main():
    copytopublic.copy_files_to_dir("./static", "./public")
    generatepage.generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()