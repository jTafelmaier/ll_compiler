



START TEXT Main
    | To "Hello"
    + hello
    | To "World"
    + world
    | To input # TODO improve this example
    | Logwithquotes "Stage 1:"
    | Split " "
    | Filter Isalphabetic
    | Map Titlecase
    | Join " "
    | Addright ": Hello World!"
    | Logwithquotes "Stage 2:"
    | If Isalphabetic Lowercase Uppercase
    | Log

    START TEXT Logwithquotes TEXT:prefix
        | Addright "\""
        | Addleft "\""
        | Addleft prefix
        | Log
        | To input

