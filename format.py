def formatResponse(response):
    presentation = []

    def find_second_occurrence(string, character):
        first_occurrence = string.find(character)
        second_occurrence = string.find(character, first_occurrence + 1)

        return second_occurrence

    pages = response.count("Header")

    for i in range(pages):
        if i == pages - 1:
            presentation.append(response)
            break
        first = response.find("Header")
        second = find_second_occurrence(response, "Header")
        presentation.append(response[first:second])
        response = response[second:]

    def form_dicts(string):

        def remove_blanks(st):
            # Remove spaces from the end
            while len(st) > 0 and st[-1] == ' ':
                st = st[:-1]

            # Remove spaces from the start
            while len(st) > 0 and st[0] == ' ':
                st = st[1:]

            return st

        def remove_newlines(st):
            if st[0] == '\n':
                st = st[1:]
            for ch in range(len(st)):
                if st[ch] == '\n':
                    st = st[:ch]
                    break
            return st

        d = {"Header": "", "Content": "", "Image": ""}
        contentIndex = string.find("Content")
        imageIndex = string.find("Image")
        d["Header"] = remove_blanks(remove_newlines(string[8:contentIndex]))
        d["Content"] = remove_blanks(remove_newlines(string[9 + contentIndex:imageIndex]))
        d["Image"] = remove_blanks(remove_newlines(string[6 + imageIndex:]))

        return d

    presentation = list(map(form_dicts, presentation))

    return presentation

