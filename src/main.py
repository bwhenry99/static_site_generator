from textnode import TextNode, TextType

def main():
    test = TextNode("dummy text", TextType.LINK, "this is a url")
    print(test)


if __name__ == "__main__":
    main()