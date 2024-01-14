



def TEXT applyFunction
    FN[TEXT > TEXT] Function

    return Input
        > Function


def TEXT applyTwoFunctionsReversed
    FN[TEXT > TEXT] Function2
    FN[TEXT > TEXT] Function1

    return Input
        > Function1
        > Function2


"Hello"
    > applyTwoFunctionsReversed [
        append "!"
        append " World"]
    > applyFunction append " c1"
    > applyTwoFunctionsReversed [
        reversed
        reversed]
    > print

