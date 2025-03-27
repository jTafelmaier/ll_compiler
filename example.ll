



def TEXT identity

    def TEXT identity2

        ----> Input
            > append ""

    ----> Input
        > identity2
        > append ""


TwoHundred = 200
    > toText

note comment

HelloWorld = "_ HelLO ;; 12 woRlD hEllo2 !"
    > append TwoHundred
    > identity
    > splitOn " "
    > retainIf isAlphabetic
    > map titlecase
    > joined ", "
    > append "!"


HelloWorld
    > prepend "Text is: "
    > print


HelloWorld
    > if
        isAlphabetic
        toOtherItem "True"
        toOtherItem "False"
    > prepend "Text is alphabetic: "
    > print

