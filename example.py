

from built_in_functions.built_in_functions import *




def main():

    def nonpython_standardise(
        nonpython_Input,
        nonpython_Separator):

        def nonpython_standardiseList(
            nonpython_Input):

            return nonpython_map(
                nonpython_retainIf(
                    nonpython_Input,
                    lambda nonpython_Input: nonpython_isAlphabetic(
                        nonpython_Input)),
                lambda nonpython_Input: nonpython_titlecase(
                    nonpython_Input))

        return nonpython_joined(
            nonpython_standardiseList(
                nonpython_splitOn(
                    nonpython_Input,
                    nonpython_Separator)),
            nonpython_Separator)

    # Nonpython Comment: this is a comment

    nonpython_HelloWorld = nonpython_append(
        nonpython_standardise(
            nonpython_prepend(
                nonpython_toText(
                    200),
                "_ HelLO ;; 12 woRlD hEllo2 !"),
            " "),
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

