



import typing

from src.auxiliary import m_common_functions
from src.auxiliary import m_shared




def get_dict_data_parsed_ll(
    list_file:typing.List):

    KEYWORD_DEFINITION_FUNCTION = "START"
    KEYWORD_DEFINITION_CLASS = "CLASS"
    KEYWORD_FUNCTION_CALL = "|"
    KEYWORD_MEMORY_WRITE = "+"

    KEY_LIST_TOKENS = "list_tokens"

    def get_dict_parsed_definition(
        list_definition:typing.List):

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
            token:typing.Union[str, typing.List]):

            if isinstance(token, list):
                text_token_first = token \
                    [0]
            else:
                text_token_first = token

            if text_token_first[0] == ":":
                return {
                    m_shared.Object_variable.KEY_TEXT_CATEGORY: m_shared.KEY_CATEGORY_MEMORY_READ,
                    m_shared.Memory_read.KEY_TEXT_KEY_MEMORY: text_token_first[1:]}

            if text_token_first[0].isalpha():
                return get_dict_parsed_function(token)

            return {
                m_shared.Object_variable.KEY_TEXT_CATEGORY: m_shared.KEY_CATEGORY_LITERAL,
                m_shared.Literal.KEY_TEXT_VALUE: text_token_first}

        def get_dict_parsed_function(
            token:typing.Union[str, typing.List]):

            if isinstance(token, list):
                list_tokens = token
            else:
                list_tokens = [token]

            text_name = list_tokens \
                [0]

            list_dicts_arguments = list(
                    map(
                        get_dict_parsed_expression,
                        list_tokens[1:]))

            if text_name.isupper():
                text_category = m_shared.KEY_CATEGORY_CLASS_CONSTRUCTOR
            elif text_name.islower():
                text_category = m_shared.KEY_CATEGORY_CLASS_ACCESS
            else:
                text_category = m_shared.KEY_CATEGORY_FUNCTION

            return {
                m_shared.Object_variable.KEY_TEXT_CATEGORY: text_category,
                m_shared.Function_reference.KEY_NAME_FUNCTION: text_name,
                m_shared.Function_reference.KEY_ARRAY_OBJECTS_ARGUMENTS: list_dicts_arguments}

        def get_dict_parsed_memory_write(
            list_tokens:typing.List[str]):

            text_key_memory = list_tokens \
                [0] \
                [1:]

            return {
                m_shared.Object_variable.KEY_TEXT_CATEGORY: m_shared.KEY_CATEGORY_MEMORY_WRITE,
                m_shared.Memory_write.KEY_TEXT_KEY_MEMORY: text_key_memory}

        def get_list_tokens_parsed_argument(
            list_tokens:typing.List):

            # TODO test
            list_tokens[-1] = list_tokens \
                [-1] \
                [1:]

            return list_tokens

        def get_dict_parsed_operation(
            dict_operation:typing.Dict):

            list_tokens = dict_operation \
                [KEY_LIST_TOKENS]

            return {
                KEYWORD_FUNCTION_CALL: get_dict_parsed_function,
                KEYWORD_MEMORY_WRITE: get_dict_parsed_memory_write} \
                [list_tokens[0]] \
                (list_tokens[1:])

        list_tokens_first = list_definition \
            [0] \
            [KEY_LIST_TOKENS]

        def get_dict_definition_class():

            def get_list_tokens_member(
                dict_member:typing.Dict):

                return dict_member \
                    [KEY_LIST_TOKENS] \
                    [1:]

            text_name_class = list_tokens_first \
                [1]

            list_lists_tokens_members = list(
                    map(
                        get_list_tokens_member,
                        list_definition \
                            [1:]))

            return {
                m_shared.Object_variable.KEY_TEXT_CATEGORY: m_shared.KEY_CATEGORY_DEFINITION_CLASS,
                m_shared.Definition_class.KEY_TEXT_NAME_CLASS: text_name_class,
                m_shared.Definition_class.KEY_ARRAY_ARRAYS_TOKENS_MEMBERS: list_lists_tokens_members}

        def get_dict_definition_function():

            text_name_function = list_tokens_first \
                [2]

            list_dicts_operations, \
            _, \
            list_lists_inner_definitions = m_common_functions.get_tuple_partitions_list(
                    list_items=list_definition \
                        [1:],
                    function_separate=is_empty_block)

            # TODO test
            list_lists_tokens_arguments = list(
                    map(
                        get_list_tokens_parsed_argument,
                        list_tokens_first \
                            [3:]))

            list_dicts_parsed_operations = list(
                    map(
                        get_dict_parsed_operation,
                        list_dicts_operations))

            list_dicts_parsed_inner_definitions = list(
                    map(
                        get_dict_parsed_definition,
                        list_lists_inner_definitions \
                            [::2]))

            return {
                m_shared.Object_variable.KEY_TEXT_CATEGORY: m_shared.KEY_CATEGORY_DEFINITION_FUNCTION,
                m_shared.Definition_function.KEY_TEXT_NAME_FUNCTION: text_name_function,
                m_shared.Definition_function.KEY_ARRAY_ARRAYS_TOKENS_ARGUMENTS: list_lists_tokens_arguments,
                m_shared.Definition_function.KEY_ARRAY_DICTS_OPERATIONS: list_dicts_parsed_operations,
                m_shared.Definition_function.KEY_ARRAY_DICTS_INNER_DEFINITIONS: list_dicts_parsed_inner_definitions}

        return {
            KEYWORD_DEFINITION_CLASS: get_dict_definition_class,
            KEYWORD_DEFINITION_FUNCTION: get_dict_definition_function} \
            [list_tokens_first[0]] \
            ()

    return get_dict_parsed_definition(list_file[4])

