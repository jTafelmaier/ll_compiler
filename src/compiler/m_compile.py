



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


def get_text_c_statement(
    text_line_ll:str):

    dict_names_functions = {
        "print": "printf"}

    object_input, \
    _, \
    text_function = text_line_ll \
        .partition("\n")

    # TODO use text_arguments
    name_function_ll, \
    _, \
    text_arguments = text_function \
        .lstrip("    > ") \
        .partition(" ")

    return (dict_names_functions \
            [name_function_ll]) \
        + "(" \
        + object_input \
        + ");"


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

    return get_text_indented(text_c_lines)


def compile_source():

    with open("hello_world.ll", "r", encoding="utf-8") as file_ll:
        text_ll = file_ll \
            .read()

    text_c = "\n\n#include <stdio.h>\n\n\n\n\nint main() {\n\n" \
        + get_text_c(text_ll) \
        + "\n\n    return 0;\n}\n\n"

    with open("hello_world.c", "w", encoding="utf-8") as file_c:
        file_c \
            .write(text_c)

    return None

