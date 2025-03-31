

from built_in_functions.built_in_functions import *




def nonpython_main(
    nonpython_Input):

    def nonpython_standardise(
        nonpython_Input,
        nonpython_Separator):

        return nonpython_joined(
            nonpython_map(
                nonpython_retainIf(
                    nonpython_splitOn(
                        nonpython_Input,
                        nonpython_Separator),
                    lambda var_lambda: nonpython_isAlphabetic(
                        var_lambda)),
                lambda var_lambda: nonpython_titlecase(
                    var_lambda)),
            nonpython_Separator)

    intermediate = nonpython_toText(
        nonpython_add(
            nonpython_toOtherItem(
                nonpython_Input,
                80),
            20))

    # Nonpython Comment: this is a comment
    nonpython_HelloWorld = nonpython_append(
        nonpython_standardise(
            nonpython_prepend(
                intermediate,
                "Hello world error_1"),
            " "),
        "!")

    return nonpython_print(
        nonpython_prepend(
            nonpython_if(
                nonpython_toOtherItem(
                    nonpython_print(
                        nonpython_prepend(
                            nonpython_HelloWorld,
                            "Text is: ")),
                    nonpython_HelloWorld),
                lambda var_lambda: nonpython_isAlphabetic(
                    var_lambda),
                lambda var_lambda: nonpython_toOtherItem(
                    var_lambda,
                    "True"),
                lambda var_lambda: nonpython_toOtherItem(
                    var_lambda,
                    "False")),
            "Text is alphabetic: "))


if __name__ == "__main__":
    nonpython_main()

