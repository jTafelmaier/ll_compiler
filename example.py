

from built_in_functions.built_in_functions import *




def main():

    def nonpython_appendTwice(
        nonpython_Input,
        nonpython_T):

        def nonpython_inner(
            nonpython_Input):

            return nonpython_append(
                nonpython_prepend(
                    nonpython_Input,
                    ""),
                "")

        return nonpython_inner(
            nonpython_inner(
                nonpython_append(
                    nonpython_append(
                        nonpython_Input,
                        nonpython_T),
                    nonpython_T)))

    # Nonpython Comment: this is a comment

    nonpython_HelloWorld = nonpython_append(
        nonpython_joined(
            nonpython_map(
                nonpython_retainIf(
                    nonpython_splitOn(
                        nonpython_appendTwice(
                            nonpython_prepend(
                                nonpython_toText(
                                    200),
                                "_ HelLO ;; 12 woRlD hEllo2 !"),
                            ""),
                        " "),
                    lambda nonpython_Input: nonpython_isAlphabetic(
                        nonpython_Input)),
                lambda nonpython_Input: nonpython_titlecase(
                    nonpython_Input)),
            ", "),
        "!")

    nonpython_print(
        nonpython_prepend(
            nonpython_HelloWorld,
            "Text is: "))

    nonpython_print(
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

    return None


if __name__ == "__main__":
    main()

