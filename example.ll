



def TEXT applyTwoFunctionsReversed
    FN[TEXT > TEXT] Function2
    FN[TEXT > TEXT] Function1

    def TEXT doNothing
        NOTHING _

        return Input

    return Input
        > doNothing "Nothing"
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
    > prepend "I say: "
    > applyTwoFunctionsReversed [
        reversed
        reversed]
    > print

