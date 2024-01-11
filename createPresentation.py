from presentation import makePresentation


def main():
    topic = input("What is the topic of this presentation?")
    pages = int(input("How many pages would you like?"))
    words = int(input("How many words per page?"))

    makePresentation(topic, pages, words)

    print("Presentation created!")


if __name__ == "__main__":
    main()
