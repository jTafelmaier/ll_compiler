

import typing

from src.auxiliary import m_common_functions
from src.auxiliary import m_shared




def get_dict_data_parsed_ll(
    list_file:typing.List):

    KEYWORD_OPERATION = "|"
    KEYWORD_MEMORY_WRITE = "+"
    KEYWORD_SEPARATOR_TYPE = ":"
    KEY_LIST_TOKENS = "list_tokens"

    def get_dict_parsed_function_definition(
        list_def:typing.List):

        def is_empty_block(
            item_block:typing.Union[typing.Dict, typing.List]):

            if isinstance(item_block, list):
                return False
            else:
                return len(
                    item_block \
                        [KEY_LIST_TOKENS]) \
                    == 0

        def get_dict_parsed_expression(
            text_expression:str):

            if text_expression[0].isupper():
                return get_dict_parsed_function([text_expression])

            if text_expression[0].islower():
                return {
                    m_shared.Object_variable.KEY_TEXT_CATEGORY: m_shared.KEY_CATEGORY_MEMORY_READ,
                    m_shared.Memory_read.KEY_TEXT_KEY_MEMORY: text_expression}

            return {
                m_shared.Object_variable.KEY_TEXT_CATEGORY: m_shared.KEY_CATEGORY_LITERAL,
                m_shared.Literal.KEY_TEXT_VALUE: text_expression}

        def get_dict_parsed_function(
            list_tokens:typing.List[str]):

            text_name = list_tokens \
                [0]

            list_dicts_arguments = list(
                    map(
                        get_dict_parsed_expression,
                        list_tokens[1:]))

            return {
                m_shared.Object_variable.KEY_TEXT_CATEGORY: m_shared.KEY_CATEGORY_FUNCTION,
                m_shared.Function_reference.KEY_NAME_FUNCTION: text_name,
                m_shared.Function_reference.KEY_ARRAY_OBJECTS_ARGUMENTS: list_dicts_arguments}

        def get_dict_parsed_memory_write(
            list_tokens:typing.List[str]):

            text_key_memory = list_tokens \
                [0]

            return {
                m_shared.Object_variable.KEY_TEXT_CATEGORY: m_shared.KEY_CATEGORY_MEMORY_WRITE,
                m_shared.Memory_write.KEY_TEXT_KEY_MEMORY: text_key_memory}

        def get_dict_parsed_operation(
            dict_operation:typing.Dict):

            list_tokens = dict_operation \
                [KEY_LIST_TOKENS]

            return {
                KEYWORD_OPERATION: get_dict_parsed_function,
                KEYWORD_MEMORY_WRITE: get_dict_parsed_memory_write} \
                [list_tokens[0]] \
                (list_tokens[1:])

        def get_dict_argument(
            text_argument:str):

            text_type_argument, \
            _, \
            text_name_argument = text_argument \
                .partition(KEYWORD_SEPARATOR_TYPE)

            return {
                m_shared.Function_definition.Argument.KEY_TEXT_NAME: text_name_argument,
                m_shared.Function_definition.Argument.KEY_TEXT_TYPE: text_type_argument}

        list_tokens_first = list_def \
            [0] \
            [KEY_LIST_TOKENS]

        _, \
        text_type_input, \
        text_name_function = list_tokens_first \
            [:3]

        list_dicts_operations, \
        _, \
        list_lists_inner_definitions = m_common_functions.get_tuple_partitions_list(
                list_items=list_def \
                    [1:],
                function_separate=is_empty_block)

        list_dicts_parsed_arguments = list(
                map(
                    get_dict_argument,
                    list_tokens_first \
                        [3:]))

        list_dicts_parsed_operations = list(
                map(
                    get_dict_parsed_operation,
                    list_dicts_operations))

        list_dicts_parsed_inner_definitions = list(
                map(
                    get_dict_parsed_function_definition,
                    list_lists_inner_definitions \
                        [::2]))

        return {
            m_shared.Function_definition.KEY_TEXT_NAME_FUNCTION: text_name_function,
            m_shared.Function_definition.KEY_TEXT_TYPE_INPUT: text_type_input,
            m_shared.Function_definition.KEY_ARRAY_DICTS_ARGUMENTS: list_dicts_parsed_arguments,
            m_shared.Function_definition.KEY_ARRAY_DICTS_OPERATIONS: list_dicts_parsed_operations,
            m_shared.Function_definition.KEY_ARRAY_DICTS_INNER_FUNCTION_DEFINITIONS: list_dicts_parsed_inner_definitions}

    return get_dict_parsed_function_definition(list_file[4])

