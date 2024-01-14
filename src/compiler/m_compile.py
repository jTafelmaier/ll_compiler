


from src.auxiliary import m_common_functions




def get_text_python_function_call(
    text_input:str,
    text_function_call_ll:str):

    def get_text_python_syntax_function_call(
        text_name_function:str,
        text_arguments_python:str):

        return "ll_" \
            + text_name_function \
            + "(\n" \
            + m_common_functions.get_text_indented_one_level(text_arguments_python) \
            + ")"

    if " " not in text_function_call_ll:
        return get_text_python_syntax_function_call(
                text_name_function=text_function_call_ll,
                text_arguments_python=text_input)

    text_name_function_ll, \
    _, \
    text_arguments_ll = text_function_call_ll \
        .partition(" ")

    def is_function_name(
        text_ll):

        return text_ll.isalpha() and text_ll[0].islower()

    def get_text_argument_python(
        text_argument_ll:str):

        text_argument_ll_first = text_argument_ll \
            .partition(" ") \
            [0]

        if not is_function_name(text_argument_ll_first):
            return text_argument_ll

        return "lambda Input: " \
            + get_text_python_function_call(
                    text_input="Input",
                    text_function_call_ll=text_argument_ll)

    # TODO refactor
    text_arguments_additional = ",\n" \
        .join(
            map(
                get_text_argument_python,
                map(
                    lambda text_argument_ll: text_argument_ll.lstrip(" "),
                    text_arguments_ll \
                        .rstrip("]") \
                        .lstrip("[") \
                        .lstrip("\n") \
                        .split("\n"))))

    text_arguments_python = text_input \
        + ",\n" \
        + text_arguments_additional

    return get_text_python_syntax_function_call(
            text_name_function=text_name_function_ll,
            text_arguments_python=text_arguments_python)


def get_text_python_function_chain(
    text_input:str,
    text_functions:str):

    list_texts_function_calls_ll = m_common_functions.get_text_unindented_one_level(text_functions) \
        .split("> ") \
        [1:]

    text_python_function_chain = text_input

    for text_function_call_ll in list_texts_function_calls_ll:
        # TODO refactor: use of .rstrip("\n")
        text_python_function_chain = get_text_python_function_call(
                text_input=text_python_function_chain,
                text_function_call_ll=text_function_call_ll \
                    .rstrip("\n"))

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
                lambda text_line_argument_ll: "ll_" \
                    + text_line_argument_ll
                        .rpartition(" ")
                        [-1],
                text_arguments_ll \
                    .split("\n")))

    text_arguments_python_final = "" if text_arguments_ll == "" else ",\n" + text_arguments_python_initial

    text_python_before_return_raw = get_text_python(text_body_ll_before_return)

    text_python_before_return_final = text_python_before_return_raw if text_python_before_return_raw == "" else text_python_before_return_raw + "\n\n"

    text_body_python = "Input" \
        + text_arguments_python_final \
        + "):\n\n" \
        + text_python_before_return_final \
        + "return " \
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


def get_text_python(
    text_ll:str):

    iterator_texts_blocks_ll = m_common_functions.get_iterator_texts_grouped_by_indentation(text_ll)

    return "\n\n" \
        .join(
            map(
                get_text_python_block,
                iterator_texts_blocks_ll))


def get_text_python_main(
    text_ll:str):

    # TODO implement: enums

    text_python = get_text_python(text_ll)

    return "\n\nfrom built_in_functions import *\n\n\n\n\ndef main():\n\n" \
        + m_common_functions.get_text_indented_one_level(text_python) \
        + "\n\n    return None\n\n\nif __name__ == \"__main__\":\n    main()\n\n"

