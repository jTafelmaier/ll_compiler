



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
    | If Isalphabetic [Addleft "ALPHA: "] [Addleft "NONALPHA: "]
    | PERSON "example@email.com" 20
    | age
    | Log

    START TEXT Logwithquotes TEXT:prefix
        | Addright "\""
        | Addleft "\""
        | Addleft prefix
        | Log
        | To input

    CLASS TEXT PERSON
        L TEXT:email
        L INTEGER:age

