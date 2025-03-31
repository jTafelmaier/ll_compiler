

from built_in_functions.built_in_functions import *




def nonpython_main(
    nonpython_Input):

    def nonpython_logWith(
        nonpython_Input,
        nonpython_TextLeft):

        return nonpython_log(
            nonpython_prepend(
                nonpython_Input,
                nonpython_TextLeft))

    intermediate = nonpython_add(
        nonpython_Input,
        " error_1")

    # Nonpython Comment: this is a comment
    nonpython_HelloWorld = nonpython_add(
        nonpython_join(
            nonpython_map(
                nonpython_filter(
                    nonpython_split(
                        intermediate,
                        " "),
                    lambda var_lambda: nonpython_isAlphabetic(
                        var_lambda)),
                lambda var_lambda: nonpython_title(
                    var_lambda)),
            " "),
        "!")

    return nonpython_logWith(
        nonpython_to(
            nonpython_logWith(
                nonpython_if(
                    nonpython_HelloWorld,
                    lambda var_lambda: nonpython_isAlphabetic(
                        var_lambda),
                    lambda var_lambda: nonpython_to(
                        var_lambda,
                        "True"),
                    lambda var_lambda: nonpython_to(
                        var_lambda,
                        "False")),
                "Text is alphabetic: "),
            nonpython_HelloWorld),
        "Text is: ")


if __name__ == "__main__":
    nonpython_main()

