



def TEXT reverseTwice
    NOTHING _

    return Input
        > reversed
        > reversed


def TEXT appendTwoTexts
    TEXT Text1
    TEXT Text2

    Text1Copy = Text1
        > append ""

    Text2Copy = Text2

    return Input
        > append Text1Copy
        > append Text2Copy
        > reverseTwice None


"Hello World!"
    > uppercase
    > appendTwoTexts
        " c1"
        " c2"
    > print

