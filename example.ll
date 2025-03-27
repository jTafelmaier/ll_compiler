



def :Text appendTwice
    :Text $T

    def :Text inner

        ----> $Input
            > prepend ""
            > append ""

    ----> $Input
        > append $T
        > append $T
        > inner
        > inner

! this is a comment

200
    > toText
    > prepend "_ HelLO ;; 12 woRlD hEllo2 !"
    > appendTwice ""
    > splitOn " "
    > retainIf isAlphabetic
    > map titlecase
    > joined ", "
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

