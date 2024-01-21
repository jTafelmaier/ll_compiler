



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


def get_iterator_texts_grouped_by_and_remove_indentation(
    text:str):

    def get_iterator_reversed_texts_grouped_by_indentation():

        iterator_reversed_texts_lines = reversed(
                text \
                    .split("\n"))

        text_block = ""

        for text_line in iterator_reversed_texts_lines:
            if text_block != "":
                text_block = "\n" \
                    + text_block

            if text_line == "":
                continue

            if text_line.startswith("    "):
                text_block = text_line \
                    [4:] \
                    + text_block
            else:
                yield text_line \
                    + text_block

                text_block = ""

    return reversed(
            list(
                get_iterator_reversed_texts_grouped_by_indentation()))

