

import typing

from src.auxiliary import m_common_functions
from src.compiler import m_shared




TEXT_PREFIX_TO_AVOID_NAME_CLASHES = "nonpython_"

def get_text_python_function_call(
    text_input:str,
    dict_function_call:typing.Dict):

    text_name_function = dict_function_call \
        [m_shared.Function_call.KEY_NAME_FUNCTION]

    list_dicts_arguments = dict_function_call \
        [m_shared.Function_call.KEY_ARRAY_OBJECTS_ARGUMENTS]

    list_texts_arguments_additional = list(
            map(
                get_text_python_item,
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

    # TODO implement: pre-return
    # TODO implement: type inference

    text_name_function = dict_def \
        [m_shared.Def.KEY_TEXT_NAME_FUNCTION]

    # text_type_input = dict_def \
    #     [m_shared.Def.KEY_TEXT_TYPE_INPUT]

    list_dicts_arguments = dict_def \
        [m_shared.Def.KEY_ARRAY_OBJECTS_ARGUMENTS]

    list_dicts_body_before_return = dict_def \
        [m_shared.Def.KEY_ARRAY_OBJECTS_BODY]

    dict_return = dict_def \
        [m_shared.Def.KEY_OBJECT_RETURN]

    def get_text_argument(
        dict_argument:typing.Dict):

        return TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
            + dict_argument \
                [m_shared.Def.Argument.KEY_TEXT_NAME]

    text_arguments_python_initial = ",\n" \
        .join(
            map(
                get_text_argument,
                list_dicts_arguments))

    text_arguments_python_final = "" if len(list_dicts_arguments) == 0 else ",\n" + text_arguments_python_initial

    text_python_before_return_raw = get_text_python(list_dicts_body_before_return)

    text_python_before_return_final = text_python_before_return_raw if text_python_before_return_raw == "" else text_python_before_return_raw + "\n\n"

    text_return_python = get_text_python_item(dict_return)

    text_body_python = TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
        + "Input" \
        + text_arguments_python_final \
        + "):\n\n" \
        + text_python_before_return_final \
        + "return " \
        + text_return_python

    return "def " \
        + TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
        + text_name_function \
        + "(\n" \
        + m_common_functions.get_text_indented_one_level(text_body_python)


def get_text_python_memory_allocation(
    dict_memory_allocation:typing.Dict):

    text_key_memory = dict_memory_allocation \
        [m_shared.Memory_allocation.KEY_TEXT_KEY_MEMORY]

    dict_item = dict_memory_allocation \
        [m_shared.Memory_allocation.KEY_OBJECT_CONTENT]

    return TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
        + text_key_memory \
        + " = " \
        + get_text_python_item(dict_item)


def get_text_python_item(
    dict_item:typing.Dict):

    def get_text_python_function_chain(
        dict_initial:typing.Dict,
        list_dicts_function_calls:typing.List[typing.Dict]):

        def get_text_initial(
            dict_initial:typing.Dict):

            text_category = dict_initial \
                ["category"]

            if text_category == "memory_read":
                return TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
                    + dict_initial \
                        [m_shared.Memory_read.KEY_TEXT_KEY_MEMORY]

            if text_category == "literal":
                return dict_initial \
                    [m_shared.Literal.KEY_TEXT_VALUE]

            if text_category == "function":
                # TODO refactor
                return "lambda " \
                    + TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
                    + "Input: " \
                    + get_text_python_function_call(
                            text_input=TEXT_PREFIX_TO_AVOID_NAME_CLASHES + "Input",
                            dict_function_call=dict_initial)

            raise Exception("dict_initial: Invalid \"category\".")

        text_python_current = get_text_initial(dict_initial)

        for dict_function_call in list_dicts_function_calls:
            text_python_current = get_text_python_function_call(
                    text_input=text_python_current,
                    dict_function_call=dict_function_call)

        return text_python_current

    dict_initial = dict_item \
        [m_shared.Item.KEY_TEXT_INITIAL_VALUE]

    list_dicts_function_calls = dict_item \
        [m_shared.Item.KEY_ARRAY_OBJECTS_FUNCTION_CALLS]

    return get_text_python_function_chain(
            dict_initial=dict_initial,
            list_dicts_function_calls=list_dicts_function_calls)


def get_text_python_block(
    dict_block:typing.Dict):

    text_category_block = dict_block \
        ["category"]

    dict_function = {
        "def": get_text_python_def,
        "memory_allocation": get_text_python_memory_allocation,
        "item": get_text_python_item}

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

    # TODO implement: function groups / namespaces
    # TODO implement: data classes
    # TODO implement: module imports
    # TODO implement: pure - modifying function differentiation
    # TODO implement: type inference
    # TODO implement: enums
    # TODO implement: integers, sets etc.

    text_python = get_text_python(dict["data"])

    return "\n\nfrom built_in_functions import *\n\n\n\n\ndef main():\n\n" \
        + m_common_functions.get_text_indented_one_level(text_python) \
        + "\n\n    return None\n\n\nif __name__ == \"__main__\":\n    main()\n\n"

