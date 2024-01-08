



def get_text_indented(
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


def get_text_c_function_applied(
    text_input:str,
    text_function:str):

    text_name_function_ll, \
    _, \
    text_arguments = text_function \
        .lstrip("    > ") \
        .partition(" ") \

    def get_list_texts_arguments():

        # TODO implement: keyword arguments
        list_texts_arguments = text_arguments \
            .lstrip("[") \
            .rstrip("]") \
            .split(", ")

        if list_texts_arguments == [""]:
            return [
                text_input]
        else:
            return [
                text_input] \
                + list_texts_arguments

    dict_names_functions = {
        "print": "printf",
        "text_reverse": "strrev"}

    text_arguments = ", " \
        .join(get_list_texts_arguments())

    return (dict_names_functions \
            [text_name_function_ll]) \
        + "(" \
        + text_arguments \
        + ")"


def get_text_c_statement(
    text_line_ll:str):

    text_input, \
    _, \
    text_functions = text_line_ll \
        .partition("\n")

    text_c_statement = text_input

    for text_function in text_functions.split("\n"):
        text_c_statement = get_text_c_function_applied(
                text_input=text_c_statement,
                text_function=text_function)

    return text_c_statement \
        + ";"


def get_text_c(
    text_ll:str):

    def get_list_texts_statements(
        text_ll:str):

        return text_ll \
            .split("\n\n")

    list_texts_statements = get_list_texts_statements(text_ll \
        .strip("\n"))

    text_c_lines = "\n\n" \
        .join(
            map(
                get_text_c_statement,
                list_texts_statements))

    # TODO add void
    return "\n\n#include <stdio.h>\n\n\n\n\nint main() {\n\n" \
        + get_text_indented(text_c_lines) \
        + "\n\n    return 0;\n}\n\n"

