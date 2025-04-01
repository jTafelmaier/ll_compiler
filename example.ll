



thread TEXT main

    | to "Hello World error_1"
    : TODO improve this example
    | split " "
    | joinByTitle
    | add "!"
    > HelloWorld
    | if
        isAlphabetic
        to "True"
        to "False"
    | logWith
        "Text is alphabetic "
        ""
    | to HelloWorld
    | logWith
        "Text is "
        ""

    thread LIST[TEXT] joinByTitle

        | filter isAlphabetic
        | map title
        | join " "

    thread TEXT logWith
        TEXT TextL
        TEXT TextR

        | prepend TextL
        | add TextR
        | log

