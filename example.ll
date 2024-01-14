



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


def TEXT prepend
    TEXT Text

    return Text
        > append Input


"Hello"
    > applyTwoFunctionsReversed [
        append "!"
        append " World"]
    > applyFunction prepend "I say: "
    > applyFunction reversed
    > applyFunction reversed
    > applyTwoFunctionsReversed [
        reversed
        reversed]
    > print

