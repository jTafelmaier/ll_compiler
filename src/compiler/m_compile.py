



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


def get_text_python_function_applied(
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

    text_arguments = ", " \
        .join(get_list_texts_arguments())

    return "ll_" \
        + text_name_function_ll \
        + "(" \
        + text_arguments \
        + ")"


def get_text_python_function_chain(
    text_input:str,
    text_functions:str):

    if text_functions == "":
        return text_input

    list_texts_functions = text_functions \
        .split("\n")

    text_python_function_chain = text_input

    for text_function in list_texts_functions:
        text_python_function_chain = get_text_python_function_applied(
                text_input=text_python_function_chain,
                text_function=text_function)

    return text_python_function_chain


def get_text_python_def(
    text_block:str):

    # TODO error: all sorts of things
    # TODO multiple blocks
    # TODO return
    # TODO multiple arguments
    # TODO type inference

    text_first_line, \
    _, \
    text_remaining_lines = text_block \
        .partition("\n")

    _, \
    text_type_input, \
    text_name_function = text_first_line \
        .split(" ")

    text_arguments_ll, \
    _, \
    text_body_function = text_remaining_lines \
        .partition("\n\n")

    text_return_python = get_text_python_do(text_body_function \
        .lstrip() \
        .replace(
            "return ",
            ""))

    text_arguments_python_initial = ",\n".join(
        map(
            lambda text_line_argument_ll: text_line_argument_ll
                .rpartition(" ")
                [-1],
            text_arguments_ll \
                .split("\n")))

    text_arguments_python_final = "" if text_arguments_ll == "" else ",\n" + text_arguments_python_initial

    text_body_python = "input" \
        + text_arguments_python_final \
        + "):\n\nreturn " \
        + text_return_python

    return "def ll_" \
        + text_name_function \
        + "(\n" \
        + get_text_indented(text_body_python)


def get_text_python_set(
    text_block:str):

    text_first_line, \
    _, \
    text_functions = text_block \
        .partition("\n")

    text_declaration_variable, \
    _, \
    text_input = text_first_line \
        .rpartition(" = ")

    text_python_function_chain = get_text_python_function_chain(
            text_input=text_input,
            text_functions=text_functions)

    return text_declaration_variable \
        + " = " \
        + text_python_function_chain


def get_text_python_do(
    text_block:str):

    text_input, \
    _, \
    text_functions = text_block \
        .partition("\n")

    return get_text_python_function_chain(
            text_input=text_input,
            text_functions=text_functions)


def get_text_python_block(
    text_block_ll:str):

    text_first_line = text_block_ll \
        .partition("\n") \
        [0]

    if text_first_line.startswith("def"):
        return get_text_python_def(text_block_ll)
    elif " = " in text_first_line:
        return get_text_python_set(text_block_ll)
    else:
        return get_text_python_do(text_block_ll)


def get_text_python(
    text_ll:str):

    # TODO implement: enums

    def get_list_texts_blocks(
        text_ll:str):

        return text_ll \
            .split("\n\n\n")

    list_texts_statements = get_list_texts_blocks(text_ll \
        .strip("\n"))

    text_python_lines = "\n\n" \
        .join(
            map(
                get_text_python_block,
                list_texts_statements))

    return "\n\nfrom built_in_functions import *\n\n\n\n\ndef main():\n\n" \
        + get_text_indented(text_python_lines) \
        + "\n\n    return None\n\n\nif __name__ == \"__main__\":\n    main()\n\n"

