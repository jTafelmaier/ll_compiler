

from built_in_functions.built_in_functions import *




def main():

    def nonpython_identity(
        nonpython_Input):

        def nonpython_identity2(
            nonpython_Input):

            return nonpython_append(
                nonpython_Input,
                "")

        return nonpython_append(
            nonpython_identity2(
                nonpython_Input),
            "")

    nonpython_TextTwoHundred = nonpython_toText(
        200)

    # Nonpython Comment: comment

    nonpython_TextHelloWorld = nonpython_append(
        nonpython_joined(
            nonpython_map(
                nonpython_retainIf(
                    nonpython_splitOn(
                        nonpython_identity(
                            nonpython_append(
                                "_ HelLO ;; 12 woRlD hEllo2 !",
                                nonpython_TextTwoHundred)),
                        " "),
                    lambda nonpython_Input: nonpython_isAlphabetic(
                        nonpython_Input)),
                lambda nonpython_Input: nonpython_titlecase(
                    nonpython_Input)),
            ", "),
        "!")

    nonpython_print(
        nonpython_prepend(
            nonpython_TextHelloWorld,
            "Text is: "))

    nonpython_print(
        nonpython_prepend(
            nonpython_if(
                nonpython_TextHelloWorld,
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

