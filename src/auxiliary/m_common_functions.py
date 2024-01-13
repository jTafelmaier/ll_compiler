



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


def get_list_texts_blocks(
    text_ll:str):

    return text_ll \
        .split("\n\n\n")

