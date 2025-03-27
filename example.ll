



def TEXT identity

    def TEXT identity2

        ----> Input
            > append ""

    ----> Input
        > identity2
        > append ""


TextTwoHundred = 200
    > toText

note comment

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

