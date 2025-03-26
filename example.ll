



def TEXT identity

    def TEXT identity2

        return Input
            > append ""

    return Input
        > identity2
        > append ""


TextTwoHundred = 200
    > toText

NOTE comment

TextHelloWorld = "_ HelLO ;; 12 woRlD hEllo2 !"
    > append TextTwoHundred
    > identity
    > splitOn " "
    > retainIf isAlphabetic
    > map titlecase
    > joined ", "
    > append "!"


TextHelloWorld
    > prepend "Text is: "
    > print


TextHelloWorld
    > if
        isAlphabetic
        toOtherItem "True"
        toOtherItem "False"
    > prepend "Text is alphabetic: "
    > print

