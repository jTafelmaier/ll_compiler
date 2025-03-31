

import typing

from src.auxiliary import m_common_functions
from src.compiler import m_shared




TEXT_PREFIX_TO_AVOID_NAME_CLASHES = "nonpython_"

TEXT_INPUT = TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
    + "Input"


def get_text_python_def(
    dict_def:typing.Dict):

    def get_text_function_call(
        text_input:str,
        dict_function:typing.Dict):

        text_name_function = dict_function \
            [m_shared.Function_reference.KEY_NAME_FUNCTION]

        list_dicts_arguments = dict_function \
            [m_shared.Function_reference.KEY_ARRAY_OBJECTS_ARGUMENTS]

        list_texts_arguments_additional = list(
                map(
                    get_text_expression,
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

    def get_text_expression(
        dict_expression:typing.Dict):

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

            # TODO error: name clashes with function "Input"
            return "lambda " \
                + TEXT_INPUT \
                + ": " \
                + get_text_function_call(
                        text_input=TEXT_INPUT,
                        dict_function=dict_function)

        text_category = dict_expression \
            [m_shared.Object_variable.KEY_TEXT_CATEGORY]

        return {
            "literal": get_text_literal,
            "memory_read": get_text_memory_read,
            "function": get_text_function} \
            [text_category] \
            (dict_expression)

    def get_text_operations():

        def get_text_comment(
            dict_comment:typing.Dict):

            return "\n" \
                .join(
                    map(
                        lambda text_comment: "# Nonpython Comment: " + text_comment,
                        dict_comment \
                            [m_shared.Comment.KEY_TEXT] \
                            .split("\n")))

        list_dicts_operations = dict_def \
            [m_shared.Function_definition.KEY_ARRAY_DICTS_OPERATIONS]

        text_python_current_expression = TEXT_INPUT

        text_python_finished_expressions = ""

        for dict_operation in list_dicts_operations:
            text_category = dict_operation \
                [m_shared.Object_variable.KEY_TEXT_CATEGORY]

            if text_category == "function":
                text_python_current_expression = get_text_function_call(
                        text_input=text_python_current_expression,
                        dict_function=dict_operation)

            if text_category == "memory_write":

                text_key_memory = dict_operation \
                    [m_shared.Memory_write.KEY_TEXT_KEY_MEMORY]

                text_python_finished_expressions = text_python_finished_expressions \
                    + TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
                    + text_key_memory \
                    + " = " \
                    + text_python_current_expression \
                    + "\n\n"

                text_python_current_expression = TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
                    + text_key_memory

            if text_category == "comment":

                # TODO duplicate code
                text_python_finished_expressions = text_python_finished_expressions \
                    + "intermediate = " \
                    + text_python_current_expression \
                    + "\n\n" \
                    + get_text_comment(dict_operation) \
                    + "\n"

                text_python_current_expression = "intermediate"

        return text_python_finished_expressions \
            + "return " \
            + text_python_current_expression

    def inner():

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
                                dict_def \
                                    [m_shared.Function_definition.KEY_ARRAY_DICTS_ARGUMENTS])))

        text_name_function = dict_def \
            [m_shared.Function_definition.KEY_TEXT_NAME_FUNCTION]

        # text_type_input = dict_def \
        #     [m_shared.Function_definition.KEY_TEXT_TYPE_INPUT]

        text_body = get_text_arguments() \
            + "):\n\n" \
            + "\n\n" \
                .join(
                    list(
                        map(
                            get_text_python_def,
                            dict_def \
                                [m_shared.Function_definition.KEY_ARRAY_DICTS_INNER_FUNCTION_DEFINITIONS])) \
                    + [get_text_operations()])

        return "def " \
            + TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
            + text_name_function \
            + "(\n" \
            + m_common_functions.get_text_indented_one_level(text_body)

    return inner()


def get_text_python_main(
    dict_def:typing.Dict):

    text_python = get_text_python_def(dict_def)

    return "\n\nfrom built_in_functions.built_in_functions import *\n\n\n\n\n" \
        + text_python \
        + "\n\n\nif __name__ == \"__main__\":\n    " \
        + TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
        + "main()\n\n"

