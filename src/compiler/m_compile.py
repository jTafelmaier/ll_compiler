

import typing




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

    text_input, \
    _, \
    text_function = text_line_ll \
        .partition("\n")

    def get_text_c_function_applied(
        text_name_function_ll:str,
        list_texts_arguments:typing.List[str]):

        text_arguments = ", " \
            .join(list_texts_arguments)

        return (dict_names_functions \
                [text_name_function_ll]) \
            + "(" \
            + text_arguments \
            + ");"

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

    return get_text_c_function_applied(
            text_name_function_ll=text_name_function_ll,
            list_texts_arguments=get_list_texts_arguments())


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

    # TODO add void
    text_c = "\n\n#include <stdio.h>\n\n\n\n\nint main() {\n\n" \
        + get_text_c(text_ll) \
        + "\n\n    return 0;\n}\n\n"

    with open("hello_world.c", "w", encoding="utf-8") as file_c:
        file_c \
            .write(text_c)

    return None

