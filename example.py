

from built_in_functions.built_in_functions import *




def nonpython_Main(
    nonpython_input):

    def nonpython_Logwithquotes(
        nonpython_input,
        nonpython_prefix):

        return nonpython_To(
            nonpython_Log(
                nonpython_Addleft(
                    nonpython_Addleft(
                        nonpython_Addright(
                            nonpython_input,
                            "\""),
                        "\""),
                    nonpython_prefix)),
            nonpython_input)

    nonpython_hello = nonpython_To(
        nonpython_input,
        "Hello")

    nonpython_world = nonpython_To(
        nonpython_hello,
        "World")

    return nonpython_Log(
        nonpython_If(
            nonpython_Logwithquotes(
                nonpython_Addright(
                    nonpython_Join(
                        nonpython_Map(
                            nonpython_Filter(
                                nonpython_Split(
                                    nonpython_Logwithquotes(
                                        nonpython_To(
                                            nonpython_world,
                                            nonpython_input),
                                        "Stage 1:"),
                                    " "),
                                nonpython_Isalphabetic),
                            nonpython_Titlecase),
                        " "),
                    ": Hello World!"),
                "Stage 2:"),
            nonpython_Isalphabetic,
            nonpython_Lowercase,
            nonpython_Uppercase))


if __name__ == "__main__":
    nonpython_main()

