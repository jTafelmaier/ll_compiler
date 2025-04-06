

import typing

from src.auxiliary import m_common_functions
from src.auxiliary import m_shared




TEXT_PREFIX_TO_AVOID_NAME_CLASHES = "nonpython_"

TEXT_INPUT = TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
    + "input"

TEXT_VAR_LAMBDA = "var_lambda"


def get_text_python_definition(
    dict_definition:typing.Dict):

    def get_text_function_call(
        text_input:str,
        dict_function:typing.Dict):

        text_name_function = dict_function \
            [m_shared.Function_reference.KEY_NAME_FUNCTION]

        list_dicts_arguments = dict_function \
            [m_shared.Function_reference.KEY_ARRAY_OBJECTS_ARGUMENTS]

        text_arguments_python = ",\n" \
            .join([
                    text_input] \
                + list(
                    map(
                        get_text_expression,
                        list_dicts_arguments)))

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

            if len(dict_function[m_shared.Function_reference.KEY_ARRAY_OBJECTS_ARGUMENTS]) == 0:
                return TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
                    + dict_function \
                        [m_shared.Function_reference.KEY_NAME_FUNCTION]

            return "lambda " \
                + TEXT_VAR_LAMBDA \
                + ": " \
                + get_text_function_call(
                        text_input=TEXT_VAR_LAMBDA,
                        dict_function=dict_function)

        text_category = dict_expression \
            [m_shared.Object_variable.KEY_TEXT_CATEGORY]

        return {
            m_shared.KEY_CATEGORY_LITERAL: get_text_literal,
            m_shared.KEY_CATEGORY_MEMORY_READ: get_text_memory_read,
            m_shared.KEY_CATEGORY_FUNCTION: get_text_function} \
            [text_category] \
            (dict_expression)

    def get_text_operations():

        list_dicts_operations = dict_definition \
            [m_shared.Definition_function.KEY_ARRAY_DICTS_OPERATIONS]

        text_python_current_expression = TEXT_INPUT

        text_python_finished_expressions = ""

        # TODO refactor
        for dict_operation in list_dicts_operations:

            text_category = dict_operation \
                [m_shared.Object_variable.KEY_TEXT_CATEGORY]

            if text_category == m_shared.KEY_CATEGORY_FUNCTION:
                text_python_current_expression = get_text_function_call(
                        text_input=text_python_current_expression,
                        dict_function=dict_operation)

            if text_category == m_shared.KEY_CATEGORY_MEMORY_WRITE:

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

        return text_python_finished_expressions \
            + "return " \
            + text_python_current_expression

    def get_list_text_variable_definitions_parsed(
        list_dicts_arguments:typing.List[typing.Dict]):

        def get_text_variable_definitions(
            dict_argument:typing.Dict):

            # TODO extend
            text_type = {
                "TEXT": "str",
                "INTEGER": "int"} \
                [dict_argument[m_shared.Argument.KEY_TEXT_TYPE]]

            return TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
                + dict_argument \
                    [m_shared.Argument.KEY_TEXT_NAME] \
                + ":" \
                + text_type

        return list(
                map(
                    get_text_variable_definitions,
                    list_dicts_arguments))

    def get_text_python_definition_class():

        text_name_class = dict_definition \
            [m_shared.Definition_class.KEY_TEXT_NAME_CLASS]

        text_members = "\n" \
            .join(
                get_list_text_variable_definitions_parsed(
                    dict_definition \
                        [m_shared.Definition_class.KEY_ARRAY_DICTS_MEMBERS]))

        return "class " \
            + TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
            + text_name_class \
            + ":\n" \
            + m_common_functions.get_text_indented_one_level(text_members)

    def get_text_python_definition_function():

        text_name_function = dict_definition \
            [m_shared.Definition_function.KEY_TEXT_NAME_FUNCTION]

        # text_type_input = dict_def \
        #     [m_shared.Definition_function.KEY_TEXT_TYPE_INPUT]

        text_arguments = ",\n" \
            .join(
                [TEXT_INPUT] \
                    + 
                    get_list_text_variable_definitions_parsed(
                        dict_definition \
                            [m_shared.Definition_function.KEY_ARRAY_DICTS_ARGUMENTS]))

        text_body = text_arguments \
            + "):\n\n" \
            + "\n\n" \
                .join(
                    list(
                        map(
                            get_text_python_definition,
                            dict_definition \
                                [m_shared.Definition_function.KEY_ARRAY_DICTS_INNER_DEFINITIONS])) \
                    + [get_text_operations()])

        return "def " \
            + TEXT_PREFIX_TO_AVOID_NAME_CLASHES \
            + text_name_function \
            + "(\n" \
            + m_common_functions.get_text_indented_one_level(text_body)

    return {
        m_shared.KEY_CATEGORY_DEFINITION_CLASS: get_text_python_definition_class,
        m_shared.KEY_CATEGORY_DEFINITION_FUNCTION: get_text_python_definition_function} \
        [dict_definition[m_shared.Object_variable.KEY_TEXT_CATEGORY]] \
        ()

def get_text_python_main(
    dict_definition:typing.Dict):

    text_python = get_text_python_definition(dict_definition)

    return "\n\nfrom built_in_functions.built_in_functions import *\n\n\n\n\n" \
        + text_python \
        + "\n\n"

