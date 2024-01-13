


from src.auxiliary import m_common_functions




def get_text_python_function_call(
    text_input:str,
    text_function:str):

    text_name_function_ll, \
    _, \
    text_arguments_ll = text_function \
        .replace(
            "\n",
            " ",
            1) \
        .partition(" ") \

    def get_list_texts_arguments_python():

        list_texts_arguments = list(
            filter(
                lambda text_argument_ll: text_argument_ll != "",
                map(
                    lambda text_argument_ll: text_argument_ll.lstrip(" "),
                    text_arguments_ll \
                        .lstrip("[") \
                        .rstrip("]") \
                        .split("\n"))))

        if list_texts_arguments == [""]:
            return [
                text_input]
        else:
            return [
                text_input] \
                + list_texts_arguments

    text_arguments_python = ", " \
        .join(get_list_texts_arguments_python())

    return "ll_" \
        + text_name_function_ll \
        + "(" \
        + text_arguments_python \
        + ")"


def get_text_python_function_chain(
    text_input:str,
    text_functions:str):

    if text_functions == "":
        return text_input

    # TODO refactor
    list_texts_functions = ("\n" 
        + text_functions) \
        .split("\n    > ") \
        [1:]

    text_python_function_chain = text_input

    for text_function in list_texts_functions:
        text_python_function_chain = get_text_python_function_call(
                text_input=text_python_function_chain,
                text_function=text_function)

    return text_python_function_chain


def get_text_python_def(
    text_block:str):

    # TODO error: all sorts of things
    # TODO multiple blocks
    # TODO return
    # TODO type inference

    text_first_line, \
    _, \
    text_remaining_lines_indented = text_block \
        .partition("\n")

    text_remaining_lines = m_common_functions.get_text_unindented_one_level(text_remaining_lines_indented)

    _, \
    text_type_input, \
    text_name_function = text_first_line \
        .split(" ")

    text_arguments_ll, \
    _, \
    text_body_ll = text_remaining_lines \
        .partition("\n\n")

    text_body_ll_before_return, \
    _, \
    text_body_ll_return = text_body_ll \
        .rpartition("\n\n")

    text_return_python = get_text_python_do(text_body_ll_return \
        .replace(
            "return ",
            ""))

    text_arguments_python_initial = ",\n" \
        .join(
            map(
                lambda text_line_argument_ll: text_line_argument_ll
                    .rpartition(" ")
                    [-1],
                text_arguments_ll \
                    .split("\n")))

    text_arguments_python_final = "" if text_arguments_ll == "" else ",\n" + text_arguments_python_initial

    # TODO multiple blocks in text_body_ll_before_return
    text_body_python = "Input" \
        + text_arguments_python_final \
        + "):\n\n" \
        + get_text_python_block(text_body_ll_before_return) \
        + "\n\nreturn " \
        + text_return_python

    return "def ll_" \
        + text_name_function \
        + "(\n" \
        + m_common_functions.get_text_indented_one_level(text_body_python)


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


def get_text_python_main(
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
        + m_common_functions.get_text_indented_one_level(text_python_lines) \
        + "\n\n    return None\n\n\nif __name__ == \"__main__\":\n    main()\n\n"

