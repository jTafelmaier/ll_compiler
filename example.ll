



def TEXT applyTwoFunctions
    FN[TEXT > TEXT] Function1
    FN[TEXT > TEXT] Function2

    return Input
        > Function1
        > Function2


"Hello"
    > append " World!"
    > uppercase
    > applyTwoFunctions [
        reversed
        reversed]
    > applyTwoFunctions [
        append " c1"
        append " c2"]
    > print

