

from built_in_functions.built_in_functions import *




def nonpython_main(
    nonpython_Input):

    def nonpython_logWith(
        nonpython_Input,
        nonpython_Text):

        return nonpython_log(
            nonpython_prepend(
                nonpython_Input,
                nonpython_Text))

    intermediate = nonpython_to(
        nonpython_Input,
        "Hello World error_1")

    # Nonpython Comment: TODO improve this example
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
        nonpython_add(
            nonpython_to(
                nonpython_log(
                    nonpython_if(
                        nonpython_HelloWorld,
                        lambda var_lambda: nonpython_isAlphabetic(
                            var_lambda),
                        lambda var_lambda: nonpython_to(
                            var_lambda,
                            "Text is alphabetic."),
                        lambda var_lambda: nonpython_to(
                            var_lambda,
                            "Text is not alphabetic."))),
                nonpython_HelloWorld),
            "\""),
        "Text is: \"")


if __name__ == "__main__":
    nonpython_main()

