



def get_text_indented_one_level(
    text:str):

    def get_text_line_indented(
        text_line:str):

        if text_line == "":
            return text_line

        return "    " \
            + text_line

    return "\n" \
        .join(
            map(
                get_text_line_indented,
                text \
                    .split("\n")))


def get_text_unindented_one_level(
    text:str):

    def get_text_line_unindented(
        text_line:str):

        if text_line == "":
            return text_line

        return text_line \
            [4:]

    return "\n" \
        .join(
            map(
                get_text_line_unindented,
                text \
                    .split("\n")))


def get_text_unindent_lines_except_first(
    text:str):

    text_first_line, \
    _, \
    text_remaining_indented = text \
        .partition("\n")

    text_remaining_unindented = get_text_unindented_one_level(text_remaining_indented)

    return text_first_line \
        + "\n" \
        + text_remaining_unindented


def get_iterator_texts_grouped_by_indentation(
    text:str):

    def get_iterator_reversed_texts_grouped_by_indentation():

        list_texts_lines = text \
            .split("\n")

        text_block = ""

        for text_line in reversed(list_texts_lines):
            if text_block != "":
                text_block = "\n" \
                    + text_block

            if text_line == "":
                continue

            text_block = text_line \
                + text_block

            if not text_line.startswith("    "):
                yield text_block

                text_block = ""

    return reversed(
        list(
            get_iterator_reversed_texts_grouped_by_indentation()))

