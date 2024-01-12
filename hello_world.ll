



def toTextCustom Text

    return input
        > toTextAppend " c1"
        > toTextAppend " c2"


set textHello = "Hello"


set textWorld = "World"


do textHello
    > toTextUppercase
    > toTextAppend " "
    > toTextAppend textWorld
    > toTextCustom
    > toTextReversed
    > toTextReversed
    > toTextAppend "!"
    > print

