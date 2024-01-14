



def TEXT applyFunction
    FN[TEXT > TEXT] Function

    return Input
        > Function


def TEXT applyTwoFunctions
    FN[TEXT > TEXT] Function1
    FN[TEXT > TEXT] Function2

    return Input
        > Function1
        > Function2


"Hello"
    > applyTwoFunctions [
        append " World"
        append "!"]
    > applyFunction append " c1"
    > applyTwoFunctions [
        reversed
        reversed]
    > print

