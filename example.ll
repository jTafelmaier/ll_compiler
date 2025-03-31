



def TEXT main

    | add " error_1"
    ! this is a comment
    | split " "
    | filter isAlphabetic
    | map title
    | join " "
    | add "!"
    > HelloWorld
    | if
        isAlphabetic
        to "True"
        to "False"
    | logWith "Text is alphabetic: "
    | to HelloWorld
    | logWith "Text is: "

    def TEXT logWith
        TEXT TextLeft

        | prepend TextLeft
        | log

