



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
    > applyFunction append " World!"
    > applyTwoFunctions [
        append " c1"
        append " c2"]
    > uppercase
    > applyTwoFunctions [
        reversed
        reversed]
    > print

