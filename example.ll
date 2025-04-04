



START TEXT Main
    | To "Hello"
    + hello
    | To "World"
    + world
    | To input # TODO improve this example
    | Logwithquotes "Stage 1:"
    | Split " "
    | Filter Isalphabetic
    | Map Title
    | Join " "
    | Addright ": Hello World!"
    | Logwithquotes "Stage 2:"
    | If
        Isalphabetic
        To "Text is alphabetic."
        To "Text is not alphabetic."
    | Log

    START TEXT Logwithquotes TEXT:prefix
        | Addright "\""
        | Addleft "\""
        | Addleft prefix
        | Log
        | To input

