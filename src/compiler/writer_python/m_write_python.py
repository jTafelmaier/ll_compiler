

import typing

from src.auxiliary import m_common_functions




def get_text_python_function_call(
    text_input:str,
    dict_function_call:typing.Dict):

    text_name_function = dict_function_call \
        ["name_function"]

    list_dicts_arguments = dict_function_call \
        ["arguments"]

    list_texts_arguments_additional = list(
            map(
                get_text_python_restricted,
                list_dicts_arguments))

    text_arguments_python = ",\n" \
        .join([
                text_input] \
            + list_texts_arguments_additional)

    return "ll_" \
        + text_name_function \
        + "(\n" \
        + m_common_functions.get_text_indented_one_level(text_arguments_python) \
        + ")"


def get_text_python_def(
    dict_def:typing.Dict):

    # TODO implement: pre-return
    # TODO implement: functions without arguments
    # TODO implement: type inference

    text_name_function = dict_def \
        ["name_function_def"]

    # text_type_input = dict_def \
    #     ["type_input"]

    list_dicts_arguments = dict_def \
        ["arguments_def"]

    list_dicts_body_before_return = dict_def \
        ["body"]

    dict_return = dict_def \
        ["restricted_return"]

    def get_text_argument(
        dict_argument:typing.Dict):

        return "ll_" \
            + dict_argument \
                ["name_argument_def"]

    text_arguments_python_initial = ",\n" \
        .join(
            map(
                get_text_argument,
                list_dicts_arguments))

    text_arguments_python_final = "" if len(list_dicts_arguments) == 0 else ",\n" + text_arguments_python_initial

    text_python_before_return_raw = get_text_python(list_dicts_body_before_return)

    text_python_before_return_final = text_python_before_return_raw if text_python_before_return_raw == "" else text_python_before_return_raw + "\n\n"

    text_return_python = get_text_python_restricted(dict_return)

    text_body_python = "ll_Input" \
        + text_arguments_python_final \
        + "):\n\n" \
        + text_python_before_return_final \
        + "return " \
        + text_return_python

    return "def ll_" \
        + text_name_function \
        + "(\n" \
        + m_common_functions.get_text_indented_one_level(text_body_python)


def get_text_python_memory_allocation(
    dict_memory_allocation:typing.Dict):

    text_key_memory = dict_memory_allocation \
        ["key_memory_allocation"]

    dict_restricted = dict_memory_allocation \
        ["restricted"]

    return "ll_" \
        + text_key_memory \
        + " = " \
        + get_text_python_restricted(dict_restricted)


def get_text_python_restricted(
    dict_restricted:typing.Dict):

    def get_text_python_function_chain(
        dict_initial:typing.Dict,
        list_dicts_function_calls:typing.List[typing.Dict]):

        def get_text_initial(
            dict_initial:typing.Dict):

            text_category = dict_initial \
                ["category"]

            if text_category == "memory_read":
                return "ll_" \
                    + dict_initial \
                        ["key_memory_read"]

            if text_category == "literal":
                return dict_initial \
                    ["value"]

            if text_category == "function":
                return "lambda ll_Input: " \
                    + get_text_python_function_call(
                            text_input="ll_Input",
                            dict_function_call=dict_initial)

            raise Exception("dict_initial: Invalid \"category\".")

        text_python_current = get_text_initial(dict_initial)

        for dict_function_call in list_dicts_function_calls:
            text_python_current = get_text_python_function_call(
                    text_input=text_python_current,
                    dict_function_call=dict_function_call)

        return text_python_current

    dict_initial = dict_restricted \
        ["initial"]

    list_dicts_function_calls = dict_restricted \
        ["function_calls"]

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
        "restricted": get_text_python_restricted}

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

    # TODO implement: enums
    # TODO error: None -> ll_None

    text_python = get_text_python(dict["data"])

    return "\n\nfrom built_in_functions import *\n\n\n\n\ndef main():\n\n" \
        + m_common_functions.get_text_indented_one_level(text_python) \
        + "\n\n    return None\n\n\nif __name__ == \"__main__\":\n    main()\n\n"

