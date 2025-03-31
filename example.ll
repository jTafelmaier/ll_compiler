



def TEXT main

    | prepend "Hello world error_1 "
    | standardise " "
    | append "!"
    save HelloWorld
    | prepend "Text is: "
    | print
    note this is a comment
    | toOtherItem HelloWorld
    | if
        isAlphabetic
        toOtherItem "True"
        toOtherItem "False"
    | prepend "Text is alphabetic: "
    | print

    def TEXT standardise
        TEXT Separator

        | splitOn Separator
        | retainIf isAlphabetic
        | map titlecase
        | joined Separator

