import copytopublic
import generatepage
import sys

def main():
    basepath = "/"
    if sys.argv[0]:
        basepath = sys.argv[0]

    copytopublic.copy_files_to_dir("./static", "./docs")
    generatepage.generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()