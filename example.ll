



def TEXT standardise
    TEXT Separator

    return Input
        | splitOn Separator
        | retainIf isAlphabetic
        | map titlecase
        | joined Separator


start 80
    | add 20
    | toText
    : this is a comment
    | prepend "_ HelLO ;; 12 woRlD hEllo2 !"
    | standardise " "
    | append "!"
    # HelloWorld
    | prepend "Text is: "
    | print


start HelloWorld
    | if
        isAlphabetic
        toOtherItem "True"
        toOtherItem "False"
    | prepend "Text is alphabetic: "
    | print

