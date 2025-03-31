

from built_in_functions.built_in_functions import *




def nonpython_main(
    nonpython_Input):

    def nonpython_printWith(
        nonpython_Input,
        nonpython_Note):

        return nonpython_print(
            nonpython_prepend(
                nonpython_Input,
                nonpython_Note))

    intermediate = nonpython_append(
        nonpython_Input,
        " error_1")

    # Nonpython Comment: this is a comment
    nonpython_HelloWorld = nonpython_append(
        nonpython_joined(
            nonpython_map(
                nonpython_retainIf(
                    nonpython_splitOn(
                        intermediate,
                        " "),
                    lambda var_lambda: nonpython_isAlphabetic(
                        var_lambda)),
                lambda var_lambda: nonpython_titlecase(
                    var_lambda)),
            " "),
        "!")

    return nonpython_printWith(
        nonpython_toOtherItem(
            nonpython_printWith(
                nonpython_if(
                    nonpython_HelloWorld,
                    lambda var_lambda: nonpython_isAlphabetic(
                        var_lambda),
                    lambda var_lambda: nonpython_toOtherItem(
                        var_lambda,
                        "True"),
                    lambda var_lambda: nonpython_toOtherItem(
                        var_lambda,
                        "False")),
                "Text is alphabetic: "),
            nonpython_HelloWorld),
        "Text is: ")


if __name__ == "__main__":
    nonpython_main()

