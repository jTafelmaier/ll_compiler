



thread TEXT main

    | to "Hello World error_1"
    : TODO improve this example
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

    thread TEXT logWith
        TEXT Text

        | prepend Text
        | log

