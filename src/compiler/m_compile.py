



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
    text_line_ll:str):

    text_type_block, \
    _, \
    text_block = text_line_ll \
        .partition(" ")

    dict_functions = {
        "set": get_text_python_set, 
        "do": get_text_python_do}

    return dict_functions \
        [text_type_block] \
        (text_block)


def get_text_python(
    text_ll:str):

    # TODO implement: enums

    def get_list_texts_statements(
        text_ll:str):

        return text_ll \
            .split("\n\n")

    list_texts_statements = get_list_texts_statements(text_ll \
        .strip("\n"))

    text_python_lines = "\n\n" \
        .join(
            map(
                get_text_python_block,
                list_texts_statements))

    return "\n\nfrom built_in_functions import *\n\n\n\ndef main():\n\n" \
        + get_text_indented(text_python_lines) \
        + "\n\n    return None\n\n\nif __name__ == \"__main__\":\n    main()\n\n"

