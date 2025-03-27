

import typing

from src.auxiliary import m_common_functions
from src.compiler import m_shared




TEXT_PREFIX_TO_AVOID_NAME_CLASHES = "nonpython_"

TEXT_INPUT = TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
    + "Input"


def get_text_python_block(
    dict_block:typing.Dict):

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
                    [TEXT_INPUT] \
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

    def get_text_python_return(
        dict_return:typing.Dict):

        return "return " \
            + get_text_python_operations(
                    dict_return 
                        [m_shared.Operations_return.KEY_OBJECT])

    def get_text_python_operations(
        dict_operations:typing.Dict):

        def get_text_python_function_call(
            text_input:str,
            dict_function:typing.Dict):

            text_name_function = dict_function \
                [m_shared.Function_reference.KEY_NAME_FUNCTION]

            list_dicts_arguments = dict_function \
                [m_shared.Function_reference.KEY_ARRAY_OBJECTS_ARGUMENTS]

            # TODO only allow expressions
            list_texts_arguments_additional = list(
                    map(
                        get_text_python_operations,
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

        def get_text_python_comment(
            dict_comment:typing.Dict):

            return "\n" \
                .join(
                    map(
                        lambda text_comment: "# Nonpython Comment: " + text_comment,
                        dict_comment \
                            [m_shared.Comment.KEY_TEXT] \
                            .split("\n")))

        def get_text_literal(
            dict_literal:typing.Dict):

            return dict_literal \
                [m_shared.Literal.KEY_TEXT_VALUE]

        def get_text_memory_read(
            dict_memory_read:typing.Dict):

            return TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
                + dict_memory_read \
                    [m_shared.Memory_read.KEY_TEXT_KEY_MEMORY]

        def get_text_function(
            dict_function:typing.Dict):

            return "lambda " \
                + TEXT_INPUT \
                + ": " \
                + get_text_python_function_call(
                        text_input=TEXT_INPUT,
                        dict_function=dict_function)

        dict_initial = dict_operations \
            [m_shared.Operations.KEY_OBJECT_INITIAL]

        list_dicts_operations = dict_operations \
            [m_shared.Operations.KEY_ARRAY_OBJECTS_OPERATIONS]

        text_category = dict_initial \
            [m_shared.Object_variable.KEY_TEXT_CATEGORY]

        text_python_current_expression = {
            "literal": get_text_literal,
            "memory_read": get_text_memory_read,
            "function": get_text_function} \
            [text_category] \
            (dict_initial)

        text_python_finished_expressions = ""

        for dict_operation in list_dicts_operations:
            text_category = dict_operation \
                [m_shared.Object_variable.KEY_TEXT_CATEGORY]

            if text_category == "function":
                text_python_current_expression = get_text_python_function_call(
                        text_input=text_python_current_expression,
                        dict_function=dict_operation)

            if text_category == "memory_write":

                text_key_memory = dict_operation \
                    [m_shared.Memory_write.KEY_TEXT_KEY_MEMORY]

                # TODO refactor
                text_python_finished_expressions = text_python_finished_expressions \
                    + TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
                    + text_key_memory \
                    + " = " \
                    + text_python_current_expression \
                    + "\n\n"

                # TODO implement: only do this if there are further operations
                text_python_current_expression = TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
                    + text_key_memory

            if text_category == "comment":

                # TODO refactor
                text_python_finished_expressions = text_python_finished_expressions \
                    + "intermediate = " \
                    + text_python_current_expression \
                    + "\n\n" \
                    + get_text_python_comment(dict_operation) \
                    + "\n"

                # TODO implement: only do this if there are further operations
                text_python_current_expression = "intermediate"

        return text_python_finished_expressions \
            + text_python_current_expression

    text_category_block = dict_block \
        [m_shared.Object_variable.KEY_TEXT_CATEGORY]

    if text_category_block == "empty":
        return None

    dict_function = {
        "def": get_text_python_def,
        "return": get_text_python_return,
        "operations": get_text_python_operations}

    return dict_function \
        [text_category_block] \
        (dict_block)


def get_text_python(
    list_dicts_blocks:typing.List[typing.Dict]):

    return "\n\n" \
        .join(
            filter(
                lambda dict_python: dict_python is not None,
                map(
                    get_text_python_block,
                    list_dicts_blocks)))


def get_text_python_main(
    dict:typing):

    text_python = get_text_python(dict["data"])

    return "\n\nfrom built_in_functions.built_in_functions import *\n\n\n\n\ndef main():\n\n" \
        + m_common_functions.get_text_indented_one_level(text_python) \
        + "\n\n    return None\n\n\nif __name__ == \"__main__\":\n    main()\n\n"

