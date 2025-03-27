



def :Text standardise
    :Text $Separator

    def :Text standardiseList

        ----> $Input
            > retainIf isAlphabetic
            > map titlecase

    ----> $Input
        > splitOn $Separator
        > standardiseList
        > joined $Separator


! this is a comment


100
    > add 100
    > toText
    > prepend "_ HelLO ;; 12 woRlD hEllo2 !"
    > standardise " "
    > append "!"
    # $HelloWorld
    > prepend "Text is: "
    > print


$HelloWorld
    > if
        isAlphabetic
        toOtherItem "True"
        toOtherItem "False"
    > prepend "Text is alphabetic: "
    > print

