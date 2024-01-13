



def TEXT appendTwoTexts
    TEXT Text1
    TEXT Text2

    Text2Copy = Text2

    return Input
        > append Text1
        > append Text2Copy

World = "World"
    > append "!"
    > uppercase

"Hello"
    > append " "
    > uppercase
    > append World
    > appendTwoTexts
        " c1"
        " c2"
    > print

