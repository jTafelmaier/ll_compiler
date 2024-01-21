

import typing

from src.auxiliary import m_common_functions
from src.compiler import m_shared




def get_dict_data_parsed_ll(
    text_ll:str):

    def get_dict_parsed_return(
        text:str):

        dict_expression = get_dict_parsed_expression(text)

        return {
            m_shared.Expression_return.KEY_TEXT_CATEGORY: "return",
            m_shared.Expression_return.KEY_OBJECT: dict_expression}

    def get_dict_parsed_def(
        text:str):

        text_header, \
        _, \
        text_body = text \
            .partition("\n\n")

        text_first_line, \
        _, \
        text_arguments = text_header \
            .partition("\n")

        text_type_input, \
        _, \
        text_name_function = text_first_line \
            .rpartition(" ")

        def get_list_dicts_arguments():

            def get_dict_argument_def(
                text_line_argument:str):

                text_type_argument, \
                _, \
                text_name_argument = text_line_argument \
                    .rpartition(" ")

                return {
                    m_shared.Function_definition.Argument.KEY_TEXT_NAME: text_name_argument,
                    m_shared.Function_definition.Argument.KEY_TEXT_TYPE: text_type_argument}

            if text_arguments == "":
                return []

            return list(
                    map(
                        get_dict_argument_def,
                        text_arguments \
                            .split("\n")))

        list_dicts_arguments = get_list_dicts_arguments()

        list_dicts_body = get_list_dicts_free_multiple(text_body)

        return {
            m_shared.Function_definition.KEY_TEXT_CATEGORY: "def",
            m_shared.Function_definition.KEY_TEXT_NAME_FUNCTION: text_name_function,
            m_shared.Function_definition.KEY_TEXT_TYPE_INPUT: text_type_input,
            m_shared.Function_definition.KEY_ARRAY_OBJECTS_ARGUMENTS: list_dicts_arguments,
            m_shared.Function_definition.KEY_ARRAY_OBJECTS_BODY: list_dicts_body}

    def get_dict_parsed_function(
        text_name:str,
        text_arguments:str):

        def get_text_arguments_final():

            if text_arguments.startswith("[") and text_arguments.endswith("]"):
                return text_arguments \
                        [1:-1] \
                        .lstrip("\n")

            return text_arguments

        list_dicts_arguments = list(
                map(
                    get_dict_parsed_expression,
                    m_common_functions.get_iterator_texts_grouped_by_and_remove_indentation(get_text_arguments_final())))

        return {
            m_shared.Function_reference.KEY_TEXT_CATEGORY: "function",
            m_shared.Function_reference.KEY_NAME_FUNCTION: text_name,
            m_shared.Function_reference.KEY_ARRAY_OBJECTS_ARGUMENTS: list_dicts_arguments}

    def get_dict_memory_allocation(
        text_key_memory:str,
        dict_expression:typing.Dict):

        return {
            m_shared.Memory_allocation.KEY_TEXT_CATEGORY: "memory_allocation",
            m_shared.Memory_allocation.KEY_TEXT_KEY_MEMORY: text_key_memory,
            m_shared.Memory_allocation.KEY_OBJECT_CONTENT: dict_expression}

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

    def get_dict_parsed_expression(
        text:str):

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

        def get_dict_parsed_function_call(
            text:str):

            assert text.startswith("> ")

            text_name_function, \
            _, \
            text_arguments = text \
                [2:] \
                .partition(" ")

            return get_dict_parsed_function(
                    text_name=text_name_function,
                    text_arguments=text_arguments)

        list_texts_grouped = list(
                m_common_functions.get_iterator_texts_grouped_by_and_remove_indentation(text))

        dict_initial = get_dict_parsed_initial(
                list_texts_grouped \
                    [0])

        list_dicts_function_calls = list(
                map(
                    get_dict_parsed_function_call,
                    list_texts_grouped \
                        [1:]))

        return {
            m_shared.Expression.KEY_TEXT_CATEGORY: "expression",
            m_shared.Expression.KEY_OBJECT_INITIAL: dict_initial,
            m_shared.Expression.KEY_ARRAY_OBJECTS_FUNCTION_CALLS: list_dicts_function_calls}

    def get_list_dicts_free_multiple(
        text:str):

        def get_dict_parsed_free(
            text_ll:str):

            if text_ll.startswith("return "):
                return get_dict_parsed_return(
                        text_ll \
                            [7:])

            if text_ll.startswith("def "):
                return get_dict_parsed_def(
                        text_ll \
                            [4:])

            text_first, \
            _, \
            text_remaining = text_ll \
                .partition(" = ")

            if text_first.isalnum() and text_remaining != "":

                assert text_first[0].isupper()

                dict_expression = get_dict_parsed_expression(text_remaining)

                return get_dict_memory_allocation(
                        text_key_memory=text_first,
                        dict_expression=dict_expression)

            return get_dict_parsed_expression(text_ll)

        iterator_texts_grouped = m_common_functions.get_iterator_texts_grouped_by_and_remove_indentation(text)

        return list(
                map(
                    get_dict_parsed_free,
                    iterator_texts_grouped))

    return {
        "data": get_list_dicts_free_multiple(text_ll)}

