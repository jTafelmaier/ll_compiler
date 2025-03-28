

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
                    lambda nonpython_Input: nonpython_isAlphabetic(
                        nonpython_Input)),
                lambda nonpython_Input: nonpython_titlecase(
                    nonpython_Input)),
            nonpython_Separator)

    intermediate = nonpython_toText(
        nonpython_add(
            80,
            20))

    # Nonpython Comment: this is a comment
    nonpython_HelloWorld = nonpython_append(
        nonpython_standardise(
            nonpython_prepend(
                intermediate,
                "Hello world error_1"),
            " "),
        "!")

    nonpython_print(
        nonpython_prepend(
            nonpython_HelloWorld,
            "Text is: "))

    return nonpython_print(
        nonpython_prepend(
            nonpython_if(
                nonpython_HelloWorld,
                lambda nonpython_Input: nonpython_isAlphabetic(
                    nonpython_Input),
                lambda nonpython_Input: nonpython_toOtherItem(
                    nonpython_Input,
                    "True"),
                lambda nonpython_Input: nonpython_toOtherItem(
                    nonpython_Input,
                    "False")),
            "Text is alphabetic: "))


if __name__ == "__main__":
    nonpython_main()

