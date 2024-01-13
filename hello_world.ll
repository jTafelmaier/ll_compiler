



def Text appendTwoTexts
    Text text1
    Text text2

    return input
        > append text1
        > append text2


world = "World"
    > append "!"
    > uppercase


"Hello"
    > append " "
    > uppercase
    > append world
    > appendTwoTexts [
        " c1"
        " c2"]
    > print

