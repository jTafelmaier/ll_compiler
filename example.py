

from built_in_functions.built_in_functions import *




def nonpython_main(
    nonpython_Input):

    def nonpython_joinByTitle(
        nonpython_Input):

        return nonpython_join(
            nonpython_map(
                nonpython_filter(
                    nonpython_Input,
                    lambda var_lambda: nonpython_isAlphabetic(
                        var_lambda)),
                lambda var_lambda: nonpython_title(
                    var_lambda)),
            " ")

    def nonpython_logWith(
        nonpython_Input,
        nonpython_Text):

        return nonpython_log(
            nonpython_prepend(
                nonpython_Input,
                nonpython_Text))

    intermediate = nonpython_add(
        nonpython_Input,
        " error_1")

    # Nonpython Comment: TODO improve this example
    nonpython_HelloWorld = nonpython_add(
        nonpython_joinByTitle(
            nonpython_split(
                intermediate,
                " ")),
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
                "Text is alphabetic "),
            nonpython_HelloWorld),
        "Text is ")


if __name__ == "__main__":
    nonpython_main()

