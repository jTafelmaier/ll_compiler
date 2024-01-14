



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
    > uppercase
    > applyTwoFunctions [
        reversed
        reversed]
    > print

