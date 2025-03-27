



def TEXT identity

    def TEXT identity2

        ----> Input
            > append ""

    ----> Input
        > identity2
        > append ""

note comment

HelloWorld = 200
    > toText
    > prepend "_ HelLO ;; 12 woRlD hEllo2 !"
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

