

import typing

from src.auxiliary import m_common_functions
from src.compiler import m_shared




def get_dict_data_parsed_ll(
    item_blocks:typing.Dict):

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

    def get_dict_parsed_return(
        list_block:typing.List):

        dict_operations = get_dict_parsed_operations(list_block)

        return {
            m_shared.Object_variable.KEY_TEXT_CATEGORY: "return",
            m_shared.Operations_return.KEY_OBJECT: dict_operations}

    def get_dict_parsed_operations(
        item_block:typing.Union[typing.Dict, typing.List]):

        list_block = get_list_block(item_block)

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
                        get_dict_parsed_operations,
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

        def get_dict_parsed_initial():

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

        def get_dict_parsed_operation(
            item_block:typing.Union[typing.Dict, typing.List]):

            list_block = get_list_block(item_block)

            list_tokens_first = get_list_tokens_first(list_block)

            text_token_first = list_tokens_first[0]

            del list_tokens_first[0]

            return {
                ">": get_dict_parsed_function,
                "save": get_dict_parsed_memory_write,
                "note": get_dict_parsed_comment} \
                [text_token_first] \
                (list_block)

        dict_initial = get_dict_parsed_initial()

        list_dicts_operations = list(
                map(
                    get_dict_parsed_operation,
                    list_block \
                        [1:]))

        return {
            m_shared.Object_variable.KEY_TEXT_CATEGORY: "operations",
            m_shared.Operations.KEY_OBJECT_INITIAL: dict_initial,
            m_shared.Operations.KEY_ARRAY_OBJECTS_OPERATIONS: list_dicts_operations}

    def get_dict_parsed_function_definition(
        list_block:typing.List):

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

        text_type_input, \
        text_name_function = get_list_tokens_first(list_block)

        list_block_arguments, \
        _, \
        list_blocks_body = m_common_functions.get_tuple_partitions_list(
                list_items=list_block[1:],
                function_separate=is_empty_block)

        list_dicts_arguments = list(
                map(
                    get_dict_argument,
                    list_block_arguments))

        list_dicts_body = get_list_dicts_multiple_blocks(list_blocks_body)

        return {
            m_shared.Object_variable.KEY_TEXT_CATEGORY: "def",
            m_shared.Function_definition.KEY_TEXT_NAME_FUNCTION: text_name_function,
            m_shared.Function_definition.KEY_TEXT_TYPE_INPUT: text_type_input,
            m_shared.Function_definition.KEY_ARRAY_OBJECTS_ARGUMENTS: list_dicts_arguments,
            m_shared.Function_definition.KEY_ARRAY_OBJECTS_BODY: list_dicts_body}

    def get_dict_block(
        item_block:typing.Union[typing.Dict, typing.List]):

        list_block = get_list_block(item_block)

        list_tokens_first = get_list_tokens_first(list_block)

        if len(list_tokens_first) == 0:
            # TODO add line index
            return {
                m_shared.Object_variable.KEY_TEXT_CATEGORY: "empty"}

        text_token_first = list_tokens_first \
            [0]

        del list_tokens_first[0]

        if text_token_first == "start":
            return get_dict_parsed_operations(list_block)

        if text_token_first == "def":
            return get_dict_parsed_function_definition(list_block)

        if text_token_first == "return":
            return get_dict_parsed_return(list_block)

        raise Exception("unknown block type")

    def get_list_dicts_multiple_blocks(
        item_blocks:typing.Union[typing.Dict, typing.List]):

        return list(
            map(
                get_dict_block,
                get_list_block(item_blocks)))

    return {
        "data": get_list_dicts_multiple_blocks(item_blocks)}

