



def TEXT main

    def TEXT standardise
        TEXT Separator

        load| Input
            | splitOn Separator
            | retainIf isAlphabetic
            | map titlecase
            | joined Separator

    load| 80
        | add 20
        | toText
        : this is a comment
        | prepend "Hello world error_1"
        | standardise " "
        | append "!"
        # HelloWorld
        | prepend "Text is: "
        | print
    load| HelloWorld
        | if
            isAlphabetic
            toOtherItem "True"
            toOtherItem "False"
        | prepend "Text is alphabetic: "
        | print

