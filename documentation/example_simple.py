



import dataclasses

from built_in_functions.built_in_functions import *




def nonpython_Main(
    nonpython_input:object):

    def nonpython_Getaveragelength(
        nonpython_input:object):

        nonpython_countItems = nonpython_Length(
            nonpython_input)

        return nonpython_Dividefloat(
            nonpython_Sum(
                nonpython_Map(
                    nonpython_To(
                        nonpython_countItems,
                        nonpython_input),
                    lambda x: nonpython_Length(
                        x))),
            nonpython_countItems)

    return nonpython_Log(
        nonpython_Getaveragelength(
            nonpython_Split(
                nonpython_To(
                    nonpython_input,
                    "Test, Hello, World"),
                ", ")))

