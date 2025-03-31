



def TEXT main

    | append " error_1"
    note this is a comment
    | splitOn " "
    | retainIf isAlphabetic
    | map titlecase
    | joined " "
    | append "!"
    save HelloWorld
    | if
        isAlphabetic
        toOtherItem "True"
        toOtherItem "False"
    | printWith "Text is alphabetic: "
    | toOtherItem HelloWorld
    | printWith "Text is: "

    def TEXT printWith
        TEXT Note

        | prepend Note
        | print

