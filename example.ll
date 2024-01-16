



def TEXT applyTwoFunctionsReversed
    FN[TEXT > TEXT] Function2
    FN[TEXT > TEXT] Function1

    def TEXT doNothing
        NOTHING _

        return Input

    return Input
        > doNothing None
        > Function1
        > Function2


def TEXT prepend
    TEXT Text

    return Text
        > append Input


Text1 = "Hello"
    > prepend ""
    > append ""


Text2 = " World"


Text1
    > applyTwoFunctionsReversed [
        append "!"
        append Text2]
    > prepend "I say: "
    > applyTwoFunctionsReversed [
        reversed
        reversed]
    > print

