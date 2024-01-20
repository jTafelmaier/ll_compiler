

from built_in_functions.built_in_functions import *




def main():

    nonpython_TextTwoHundred = nonpython_toText(
        200)

    nonpython_TextHelloWorld = nonpython_append(
        nonpython_joined(
            nonpython_map(
                nonpython_retainIf(
                    nonpython_splitOn(
                        nonpython_append(
                            "_ HelLO ;; 12 woRlD hEllo2 !",
                            nonpython_TextTwoHundred),
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

