



chain TEXT main
    | to "Hello World error_1" # TODO improve this example
    | split " "
    | filter isAlphabetic
    | map title
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

