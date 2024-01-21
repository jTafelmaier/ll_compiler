

import typing

from src.auxiliary import m_common_functions
from src.compiler import m_shared




TEXT_PREFIX_TO_AVOID_NAME_CLASHES = "nonpython_"

def get_text_python_function_call(
    text_input:str,
    dict_function_call:typing.Dict):

    text_name_function = dict_function_call \
        [m_shared.Function_reference.KEY_NAME_FUNCTION]

    list_dicts_arguments = dict_function_call \
        [m_shared.Function_reference.KEY_ARRAY_OBJECTS_ARGUMENTS]

    list_texts_arguments_additional = list(
            map(
                get_text_python_expression,
                list_dicts_arguments))

    text_arguments_python = ",\n" \
        .join([
                text_input] \
            + list_texts_arguments_additional)

    return TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
        + text_name_function \
        + "(\n" \
        + m_common_functions.get_text_indented_one_level(text_arguments_python) \
        + ")"


def get_text_python_def(
    dict_def:typing.Dict):

    text_name_function = dict_def \
        [m_shared.Function_definition.KEY_TEXT_NAME_FUNCTION]

    # text_type_input = dict_def \
    #     [m_shared.Function_definition.KEY_TEXT_TYPE_INPUT]

    list_dicts_arguments = dict_def \
        [m_shared.Function_definition.KEY_ARRAY_OBJECTS_ARGUMENTS]

    # TODO ensure at least one return
    list_dicts_body = dict_def \
        [m_shared.Function_definition.KEY_ARRAY_OBJECTS_BODY]

    def get_text_arguments():

        def get_text_argument(
            dict_argument:typing.Dict):

            return TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
                + dict_argument \
                    [m_shared.Function_definition.Argument.KEY_TEXT_NAME]

        return ",\n" \
            .join(
                [
                    TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
                        + "Input"] \
                    + list(
                        map(
                            get_text_argument,
                            list_dicts_arguments)))

    text_body = get_text_arguments() \
        + "):\n\n" \
        + get_text_python(list_dicts_body)

    return "def " \
        + TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
        + text_name_function \
        + "(\n" \
        + m_common_functions.get_text_indented_one_level(text_body)


def get_text_python_memory_allocation(
    dict_memory_allocation:typing.Dict):

    text_key_memory = dict_memory_allocation \
        [m_shared.Memory_allocation.KEY_TEXT_KEY_MEMORY]

    dict_expression = dict_memory_allocation \
        [m_shared.Memory_allocation.KEY_OBJECT_CONTENT]

    return TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
        + text_key_memory \
        + " = " \
        + get_text_python_expression(dict_expression)


def get_text_python_return(
    dict_return:typing.Dict):

    return "return " \
        + get_text_python_expression(
                dict_return 
                    [m_shared.Expression_return.KEY_OBJECT])


def get_text_python_expression(
    dict_expression:typing.Dict):

    def get_text_initial(
        dict_initial:typing.Dict):

        text_category = dict_initial \
            [m_shared.Object_variable.KEY_TEXT_CATEGORY]

        if text_category == "memory_read":
            return TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
                + dict_initial \
                    [m_shared.Memory_read.KEY_TEXT_KEY_MEMORY]

        if text_category == "literal":
            return dict_initial \
                [m_shared.Literal.KEY_TEXT_VALUE]

        if text_category == "function":
            text_input = TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
                + "Input"

            return "lambda " \
                + TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
                + "Input: " \
                + get_text_python_function_call(
                        text_input=text_input,
                        dict_function_call=dict_initial)

        raise Exception(
                "dict_initial: Invalid \"" \
                    + m_shared.Object_variable.KEY_TEXT_CATEGORY \
                    + "\".")

    dict_initial = dict_expression \
        [m_shared.Expression.KEY_OBJECT_INITIAL]

    list_dicts_function_calls = dict_expression \
        [m_shared.Expression.KEY_ARRAY_OBJECTS_FUNCTION_CALLS]

    text_python_current = get_text_initial(dict_initial)

    for dict_function_call in list_dicts_function_calls:
        text_python_current = get_text_python_function_call(
                text_input=text_python_current,
                dict_function_call=dict_function_call)

    return text_python_current


def get_text_python_block(
    dict_block:typing.Dict):

    text_category_block = dict_block \
        [m_shared.Object_variable.KEY_TEXT_CATEGORY]

    dict_function = {
        "def": get_text_python_def,
        "memory_allocation": get_text_python_memory_allocation,
        "return": get_text_python_return,
        "expression": get_text_python_expression}

    return dict_function \
        [text_category_block] \
        (dict_block)


def get_text_python(
    list_dicts_blocks:typing.List[typing.Dict]):

    return "\n\n" \
        .join(
            map(
                get_text_python_block,
                list_dicts_blocks))


def get_text_python_main(
    dict:typing):

    text_python = get_text_python(dict["data"])

    return "\n\nfrom built_in_functions.built_in_functions import *\n\n\n\n\ndef main():\n\n" \
        + m_common_functions.get_text_indented_one_level(text_python) \
        + "\n\n    return None\n\n\nif __name__ == \"__main__\":\n    main()\n\n"

