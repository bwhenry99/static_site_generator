import copytopublic
import generatepage

def main():
    copytopublic.copy_files_to_dir("./static", "./public")
    generatepage.generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()