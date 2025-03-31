



def TEXT main

    | toOtherItem 80
    | add 20
    | toText
    note this is a comment
    | prepend "Hello world error_1"
    | standardise " "
    | append "!"
    save HelloWorld
    | prepend "Text is: "
    | print
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

