



import dataclasses

from built_in_functions.built_in_functions import *




def nonpython_Main(
    nonpython_input:object):

    def nonpython_Getaverage(
        nonpython_input:object):

        nonpython_countItems = nonpython_Length(
            nonpython_input)

        return nonpython_Dividefloat(
            nonpython_Sum(
                nonpython_To(
                    nonpython_countItems,
                    nonpython_input)),
            nonpython_countItems)

    return nonpython_Log(
        nonpython_Getaverage(
            nonpython_Map(
                nonpython_Filter(
                    nonpython_Split(
                        nonpython_To(
                            nonpython_input,
                            "Test, Hello, World, 00"),
                        ", "),
                    lambda x: nonpython_Isalphabetic(
                        x)),
                lambda x: nonpython_Length(
                    x))))

