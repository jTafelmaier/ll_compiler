



def toTextCustom Text
    arg textToAppend

    return input
        > toTextAppend textToAppend
        > toTextAppend textToAppend


set textHello = "Hello"


set textWorld = "World"


do textHello
    > toTextUppercase
    > toTextAppend " "
    > toTextAppend textWorld
    > toTextCustom " c"
    > toTextReversed
    > toTextReversed
    > toTextAppend "!"
    > print

