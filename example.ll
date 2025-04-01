



thread TEXT main

    | add " error_1"
    : TODO improve this example
    | split " "
    | joinByTitle
    | add "!"
    > HelloWorld
    | if
        isAlphabetic
        to "True"
        to "False"
    | logWith "Text is alphabetic "
    | to HelloWorld
    | logWith "Text is "

    thread LIST[TEXT] joinByTitle

        | filter isAlphabetic
        | map title
        | join " "

    thread TEXT logWith
        TEXT Text

        | prepend Text
        | log

