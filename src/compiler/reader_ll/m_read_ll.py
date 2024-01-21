

import typing

from src.auxiliary import m_common_functions
from src.compiler import m_shared




def get_dict_data_parsed_ll(
    text_ll:str):

    def get_dict_parsed_def(
        text_full:str):

        text_header, \
        _, \
        text_body = text_full \
            .partition("\n\n")

        text_first_line, \
        _, \
        text_arguments = text_header \
            .partition("\n")

        text_type_input, \
        _, \
        text_name_function = text_first_line \
            [4:] \
            .rpartition(" ")

        def get_list_dicts_arguments():

            def get_dict_argument_def(
                text_line_argument:str):

                text_type_argument, \
                _, \
                text_name_argument = text_line_argument \
                    .rpartition(" ")

                return {
                    m_shared.Def.Argument.KEY_TEXT_NAME: text_name_argument,
                    m_shared.Def.Argument.KEY_TEXT_TYPE: text_type_argument}

            if text_arguments == "":
                return []

            return list(
                    map(
                        get_dict_argument_def,
                        text_arguments \
                            .split("\n")))

        list_dicts_arguments = get_list_dicts_arguments()

        text_pre_return, \
        _, \
        text_return = text_body \
            .rpartition("return ")

        list_dicts_body = get_list_dicts_free_multiple(text_pre_return)

        text_return_full_edited = m_common_functions.get_text_unindent_lines_except_first(text_return)

        dict_return = get_dict_parsed_item(text_return_full_edited)

        return {
            m_shared.Def.KEY_TEXT_CATEGORY: "def",
            m_shared.Def.KEY_TEXT_NAME_FUNCTION: text_name_function,
            m_shared.Def.KEY_TEXT_TYPE_INPUT: text_type_input,
            m_shared.Def.KEY_ARRAY_OBJECTS_ARGUMENTS: list_dicts_arguments,
            m_shared.Def.KEY_ARRAY_OBJECTS_BODY: list_dicts_body,
            m_shared.Def.KEY_OBJECT_RETURN: dict_return}

    def get_dict_parsed_function(
        text_name:str,
        text_arguments:str):

        def get_dict_argument(
            text_argument:str):

            text_argument_edited = m_common_functions.get_text_unindent_lines_except_first(text_argument)

            return get_dict_parsed_item(text_argument_edited)

        def get_text_arguments_final():

            if text_arguments.startswith("[") and text_arguments.endswith("]"):
                return m_common_functions.get_text_unindented_one_level(
                        text_arguments \
                            [1:-1] \
                            .lstrip("\n"))

            return text_arguments

        list_dicts_arguments = list(
                map(
                    get_dict_argument,
                    m_common_functions.get_iterator_texts_grouped_by_indentation(get_text_arguments_final())))

        return {
            m_shared.Function_Item.KEY_TEXT_CATEGORY: "function",
            m_shared.Function_Item.KEY_NAME_FUNCTION: text_name,
            m_shared.Function_Item.KEY_ARRAY_OBJECTS_ARGUMENTS: list_dicts_arguments}

    def get_dict_parsed_function_call(
        text_function_call:str):

        assert text_function_call.startswith("> ")

        text_name_function, \
        _, \
        text_arguments = text_function_call \
            [2:] \
            .partition(" ")

        # TODO test
        return get_dict_parsed_function(
                text_name=text_name_function,
                text_arguments=text_arguments)

    def get_dict_memory_allocation(
        text_key_memory:str,
        dict_item:typing.Dict):

        return {
            m_shared.Memory_allocation.KEY_TEXT_CATEGORY: "memory_allocation",
            m_shared.Memory_allocation.KEY_TEXT_KEY_MEMORY: text_key_memory,
            m_shared.Memory_allocation.KEY_OBJECT_CONTENT: dict_item}

    def get_dict_parsed_memory_read(
        text:str):

        return {
            m_shared.Memory_read.KEY_TEXT_CATEGORY: "memory_read",
            m_shared.Memory_read.KEY_TEXT_KEY_MEMORY: text}

    def get_dict_parsed_literal(
        text:str):

        return {
            m_shared.Literal.KEY_TEXT_CATEGORY: "literal",
            m_shared.Literal.KEY_TEXT_VALUE: text}

    def get_dict_parsed_item(
        text_full:str):

        set_texts_special_literals = {
            "None",
            "True",
            "False"}

        def get_dict_parsed_initial(
            text:str):

            text_first, \
            _, \
            text_second = text \
                .partition(" ")

            if text.startswith("[") and text.endswith("]"):
                # TODO separate list category
                # TODO allow memory read (variables) in lists
                return get_dict_parsed_literal(text)

            if text_first in set_texts_special_literals:
                return get_dict_parsed_literal(text_first)

            if text_first[0].isupper():
                return get_dict_parsed_memory_read(text)

            if text_first.isnumeric():
                return get_dict_parsed_literal(text_first)

            if text_first.isalnum():
                return get_dict_parsed_function(
                        text_name=text_first,
                        text_arguments=text_second)

            return get_dict_parsed_literal(text)

        list_texts_grouped = list(
                m_common_functions.get_iterator_texts_grouped_by_indentation(text_full))

        # TODO test further: always at least one item in list?
        dict_initial = get_dict_parsed_initial(
                list_texts_grouped \
                    [0])

        list_dicts_function_calls = list(
                map(
                    get_dict_parsed_function_call,
                    list_texts_grouped \
                        [1:]))

        return {
            m_shared.Item.KEY_TEXT_CATEGORY: "item",
            m_shared.Item.KEY_TEXT_INITIAL_VALUE: dict_initial,
            m_shared.Item.KEY_ARRAY_OBJECTS_FUNCTION_CALLS: list_dicts_function_calls}

    def get_dict_parsed_free(
        text_ll:str):

        text_full_edited = m_common_functions.get_text_unindent_lines_except_first(text_ll)

        # TODO perhaps implement: string

        if text_full_edited.startswith("def "):
            return get_dict_parsed_def(text_full_edited)

        text_first, \
        _, \
        text_remaining = text_full_edited \
            .partition(" = ")

        # TODO test
        if text_first.isalnum() and text_first[0].isupper() and text_remaining != "":
            dict_item = get_dict_parsed_item(text_remaining)

            return get_dict_memory_allocation(
                    text_key_memory=text_first,
                    dict_item=dict_item)

        return get_dict_parsed_item(text_full_edited)

    def get_list_dicts_free_multiple(
        text:str):

        iterator_texts_grouped = m_common_functions.get_iterator_texts_grouped_by_indentation(text)

        return list(
                map(
                    get_dict_parsed_free,
                    iterator_texts_grouped))

    return {
        "data": get_list_dicts_free_multiple(text_ll)}

