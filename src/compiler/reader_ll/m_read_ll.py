

import typing

from src.auxiliary import m_common_functions




def get_list_items_ll_parsed(
    text_ll:str):

    def get_dict_parsed_def(
        text_first_line:str,
        text_remaining:str):

        text_type_input, \
        _, \
        text_name_function = text_first_line \
            [4:] \
            .rpartition(" ")

        text_arguments, \
        _, \
        text_body = text_remaining \
            .partition("\n\n")

        def get_dict_argument_def(
            text_line_argument:str):

            text_type_argument, \
            _, \
            text_name_argument = text_line_argument \
                .rpartition(" ")

            return {
                "name": text_name_argument,
                "type": text_type_argument}

        list_dicts_arguments = list(
                map(
                    get_dict_argument_def,
                    text_arguments \
                        .split("\n")))

        text_pre_return, \
        _, \
        text_return = text_body \
            .rpartition("return ")

        list_dicts_body = get_list_dicts_free_multiple(text_pre_return)

        text_return_first_line, \
        _, \
        text_return_remaining_indented = text_return \
            .partition("\n")

        dict_return = get_dict_parsed_restricted(
                text_first_line=text_return_first_line,
                text_remaining=m_common_functions.get_text_unindented_one_level(text_return_remaining_indented))

        return {
            "category": "def",
            "name": text_name_function,
            "type_input": text_type_input,
            "arguments": list_dicts_arguments,
            "body": list_dicts_body,
            "return": dict_return}

    def get_dict_parsed_function_call(
        text_function_call:str):

        assert text_function_call.startswith("> ")

        name_function, \
        _, \
        text_arguments = text_function_call \
            [2:] \
            .partition(" ")

        def get_dict_argument(
            text_argument:str):

            text_first_line, \
            _, \
            text_remaining_indented = text_argument \
                .partition("\n")

            return get_dict_parsed_restricted(
                    text_first_line=text_first_line,
                    text_remaining=m_common_functions.get_text_unindented_one_level(text_remaining_indented))

        def get_text_arguments_final():

            if text_arguments.startswith("[") and text_arguments.endswith("]"):
                return m_common_functions.get_text_unindented_one_level(
                        text_arguments \
                            [1:-1] \
                            .lstrip("\n"))
            else:
                return text_arguments

        list_dicts_arguments = list(
                map(
                    get_dict_argument,
                    m_common_functions.get_iterator_texts_grouped_by_indentation(get_text_arguments_final())))

        return {
            "name_function": name_function,
            "arguments": list_dicts_arguments}

    def get_dict_parsed_variable(
        text:str):

        return {
            "category": "variable",
            "name": text}

    def get_dict_parsed_function(
        text_name:str,
        text_arguments:str):

        return {
            "category": "function",
            "name": text_name,
            "arguments": text_arguments}

    def get_dict_parsed_literal(
        text:str):

        return {
            "category": "literal",
            "value": text}

    def get_dict_parsed_item(
        text:str):

        text_first, \
        _, \
        text_second = text \
            .partition(" ")

        if text_first[0].isupper():
            return get_dict_parsed_variable(text)

        if text_first.isalnum():
            return get_dict_parsed_function(
                    text_name=text_first,
                    text_arguments=text_second)

        return get_dict_parsed_literal(text)

    def get_dict_memory_allocation(
        text_id_memory:str,
        dict_restricted:typing.Dict):

        return {
            "category": "memory_allocation",
            "id_memory": text_id_memory,
            "restricted": dict_restricted}

    def get_dict_parsed_restricted(
        text_first_line:str,
        text_remaining:str):

        dict_first_line = get_dict_parsed_item(text_first_line)

        list_dicts_function_calls = list(
                map(
                    get_dict_parsed_function_call,
                    m_common_functions.get_iterator_texts_grouped_by_indentation(text_remaining)))

        return {
            "category": "restricted",
            "item": dict_first_line,
            "function_calls": list_dicts_function_calls}

    def get_dict_parsed_free(
        text_ll:str):

        text_first_line, \
        _, \
        text_remaining_indented = text_ll \
            .partition("\n")

        text_remaining_unindented = m_common_functions.get_text_unindented_one_level(text_remaining_indented)

        # TODO perhaps implement: string

        if text_first_line.startswith("def "):
            return get_dict_parsed_def(
                    text_first_line=text_first_line,
                    text_remaining=text_remaining_unindented)

        text_first, \
        _, \
        text_second = text_first_line \
            .partition(" = ")

        if text_first.isalnum() and text_first[0].isupper() and text_second != "":
            dict_restricted = get_dict_parsed_restricted(
                    text_first_line=text_second,
                    text_remaining=text_remaining_unindented)

            return get_dict_memory_allocation(
                    text_id_memory=text_first,
                    dict_restricted=dict_restricted)

        return get_dict_parsed_restricted(
                text_first_line=text_first_line,
                text_remaining=text_remaining_unindented)

    def get_list_dicts_free_multiple(
        text:str):

        iterator_texts_grouped = m_common_functions.get_iterator_texts_grouped_by_indentation(text)

        return list(
                map(
                    get_dict_parsed_free,
                    iterator_texts_grouped))

    return get_list_dicts_free_multiple(text_ll)

