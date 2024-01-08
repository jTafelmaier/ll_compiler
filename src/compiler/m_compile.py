



def get_text_indented(
    text:str):

    def get_text_line_indented(
        text_line:str):

        if text_line == "":
            return text_line

        return "    " \
            + text_line

    return "\n" \
        .join(
            map(
                get_text_line_indented,
                text \
                    .split("\n")))


def get_text_c_function_applied(
    text_input:str,
    text_function:str):

    text_name_function_ll, \
    _, \
    text_arguments = text_function \
        .lstrip("    > ") \
        .partition(" ") \

    def get_list_texts_arguments():

        # TODO implement: keyword arguments
        list_texts_arguments = text_arguments \
            .lstrip("[") \
            .rstrip("]") \
            .split(", ")

        if list_texts_arguments == [""]:
            return [
                text_input]
        else:
            return [
                text_input] \
                + list_texts_arguments

    dict_names_functions = {
        "print": "printf",
        "text_reverse": "strrev"}

    text_arguments = ", " \
        .join(get_list_texts_arguments())

    return (dict_names_functions \
            [text_name_function_ll]) \
        + "(" \
        + text_arguments \
        + ")"


def get_text_c_statement(
    text_line_ll:str):

    text_first_line, \
    _, \
    text_functions = text_line_ll \
        .partition("\n")

    text_declaration_variable, \
    _, \
    text_input = text_first_line \
        .rpartition(" = ")

    text_c_statement = text_input

    if text_functions != "":

        list_texts_functions = text_functions \
            .split("\n")

        for text_function in list_texts_functions:
            text_c_statement = get_text_c_function_applied(
                    text_input=text_c_statement,
                    text_function=text_function)

    text_function_result = text_c_statement \
        + ";"

    def get_text_type_final():

        if text_functions == "":
            if text_c_statement.startswith("\"") and text_c_statement.endswith("\""):
                return "Type_text"

            elif text_c_statement.isalpha():
                # TODO implement: retrieve type from variable definition
                raise NotImplementedError()

            elif text_c_statement.isdecimal():
                return "Type_decimal"

            # TODO implement: more literal types
            else:
                raise SyntaxError("Unknown literal type")

        # TODO implement: compute types from function chain
        raise NotImplementedError()

    def get_text_c_declaration_variable():

        # TODO implement: other types

        if text_declaration_variable == "":
            return ""

        text_type_final = get_text_type_final()

        if text_type_final == "Type_text":
            return "char " \
                + text_declaration_variable \
                + "[] = "

        if text_type_final == "Type_decimal":
            return "int " \
                + text_declaration_variable \
                + " = "

        raise SyntaxError("Invalid type")

    return get_text_c_declaration_variable() \
        + text_function_result


def get_text_c(
    text_ll:str):

    # TODO implement: enums

    def get_list_texts_statements(
        text_ll:str):

        return text_ll \
            .split("\n\n")

    list_texts_statements = get_list_texts_statements(text_ll \
        .strip("\n"))

    text_c_lines = "\n\n" \
        .join(
            map(
                get_text_c_statement,
                list_texts_statements))

    return "\n\n#include <stdio.h>\n#include <stdlib.h>\n\n\n\n\nint main(void) {\n\n" \
        + get_text_indented(text_c_lines) \
        + "\n\n    return EXIT_SUCCESS;\n}\n\n"

