



def :Text standardise
    :Text $Separator

    ----> $Input
        > splitOn $Separator
        > retainIf isAlphabetic
        > map titlecase
        > joined $Separator


100
    > add 100
    > toText
    ! this is a comment
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

