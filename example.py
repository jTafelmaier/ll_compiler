

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

    nonpython_HelloWorld = nonpython_add(
        nonpython_join(
            nonpython_map(
                nonpython_filter(
                    nonpython_split(
                        nonpython_to(
                            nonpython_Input,
                            "Hello World error_1"),
                        " "),
                    nonpython_isAlphabetic),
                nonpython_title),
            " "),
        "!")

    return nonpython_logWith(
        nonpython_add(
            nonpython_to(
                nonpython_log(
                    nonpython_if(
                        nonpython_HelloWorld,
                        nonpython_isAlphabetic,
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

