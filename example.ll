



chain TEXT main
    | to "Hello World error_1"
    | split " "
    | filter isAlphabetic
    | map title # TODO improve this example
    | join " "
    | add "!"
    > HelloWorld
    | if
        isAlphabetic
        to "Text is alphabetic."
        to "Text is not alphabetic."
    | log
    | to HelloWorld
    | add "\""
    | logWith "Text is: \""

    chain TEXT logWith TEXT:Text
        | prepend Text
        | log

