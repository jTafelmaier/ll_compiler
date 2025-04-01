

import typing

from src.auxiliary import m_common_functions
from src.compiler import m_shared




def get_dict_data_parsed_ll(
    list_file:typing.List):

    KEY_LIST_TOKENS = "list_tokens"

    def get_list_tokens_first(
        list_block:typing.List):

        return list_block \
            [0] \
            [KEY_LIST_TOKENS]

    def get_list_block(
        item_block:typing.Union[typing.Dict, typing.List]):

        if isinstance(item_block, dict):
            return [item_block]
        else:
            return item_block

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

        def get_dict_argument(
            dict_block_argument:typing.Dict):

            text_type_argument, \
            text_name_argument = dict_block_argument \
                [KEY_LIST_TOKENS]

            return {
                m_shared.Function_definition.Argument.KEY_TEXT_NAME: text_name_argument,
                m_shared.Function_definition.Argument.KEY_TEXT_TYPE: text_type_argument}

        def get_dict_parsed_expression(
            item_block:typing.Union[typing.Dict, typing.List]):

            list_block = get_list_block(item_block)

            text_first = get_list_tokens_first(list_block) \
                [0]

            if text_first[0].islower():
                return get_dict_parsed_function(list_block[:1])

            if text_first[0].isupper():
                return {
                    m_shared.Object_variable.KEY_TEXT_CATEGORY: "memory_read",
                    m_shared.Memory_read.KEY_TEXT_KEY_MEMORY: text_first}

            return {
                m_shared.Object_variable.KEY_TEXT_CATEGORY: "literal",
                m_shared.Literal.KEY_TEXT_VALUE: text_first}

        def get_dict_parsed_function(
            list_block:typing.List):

            list_tokens_first = get_list_tokens_first(list_block)

            text_name = list_tokens_first \
                [0]

            del list_tokens_first[0]

            if len(list_tokens_first) == 0:
                del list_block[0]

            list_dicts_arguments = list(
                    map(
                        get_dict_parsed_expression,
                        list_block))

            return {
                m_shared.Object_variable.KEY_TEXT_CATEGORY: "function",
                m_shared.Function_reference.KEY_NAME_FUNCTION: text_name,
                m_shared.Function_reference.KEY_ARRAY_OBJECTS_ARGUMENTS: list_dicts_arguments}

        def get_dict_parsed_memory_write(
            list_block:typing.List):

            text_key_memory = get_list_tokens_first(list_block) \
                [0]

            return {
                m_shared.Object_variable.KEY_TEXT_CATEGORY: "memory_write",
                m_shared.Memory_write.KEY_TEXT_KEY_MEMORY: text_key_memory}

        def get_dict_parsed_comment(
            list_block:typing.List):

            def get_text_unmodified(
                item_block:typing.Union[typing.Dict, typing.List]):

                if isinstance(item_block, dict):
                    return " " \
                        .join(item_block \
                            [KEY_LIST_TOKENS])
                else:
                    return "\n" \
                        .join(
                            map(
                                get_text_unmodified,
                                item_block))

            text = get_text_unmodified(list_block)

            return {
                m_shared.Object_variable.KEY_TEXT_CATEGORY: "comment",
                m_shared.Comment.KEY_TEXT: text}

        def get_dict_parsed_operation(
            item_block:typing.Union[typing.Dict, typing.List]):

            list_block = get_list_block(item_block)

            list_tokens_first = get_list_tokens_first(list_block)

            text_token_first = list_tokens_first[0]

            del list_tokens_first[0]

            return {
                "|": get_dict_parsed_function,
                ">": get_dict_parsed_memory_write,
                ":": get_dict_parsed_comment} \
                [text_token_first] \
                (list_block)

        _, \
        text_type_input, \
        text_name_function = get_list_tokens_first(list_def)

        list_arguments, \
        _, \
        list_blocks_body = m_common_functions.get_tuple_partitions_list(
                list_items=list_def[1:],
                function_separate=is_empty_block)

        list_dicts_arguments = list(
                map(
                    get_dict_argument,
                    list_arguments))

        list_items_operations, \
        _, \
        list_lists_function_definitions = m_common_functions.get_tuple_partitions_list(
                list_items=list_blocks_body,
                function_separate=is_empty_block)

        list_dicts_inner_definitions = list(
            map(
                get_dict_parsed_function_definition,
                list_lists_function_definitions[::2]))

        list_dicts_operations = list(
                map(
                    get_dict_parsed_operation,
                    list_items_operations))

        return {
            m_shared.Function_definition.KEY_TEXT_NAME_FUNCTION: text_name_function,
            m_shared.Function_definition.KEY_TEXT_TYPE_INPUT: text_type_input,
            m_shared.Function_definition.KEY_ARRAY_DICTS_ARGUMENTS: list_dicts_arguments,
            m_shared.Function_definition.KEY_ARRAY_DICTS_OPERATIONS: list_dicts_operations,
            m_shared.Function_definition.KEY_ARRAY_DICTS_INNER_FUNCTION_DEFINITIONS: list_dicts_inner_definitions}

    return get_dict_parsed_function_definition(list_file[4])

