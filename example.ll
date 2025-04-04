



START TEXT Main
    | To "Hello"
    + hello
    | To "World"
    + world
    | To Input
    | To Input
    | Logwithquotes "Stage 1:"
    | Split " "
    | Filter Isalphabetic
    | Map Title # TODO improve this example
    | Join " "
    | Addright ": Hello World!"
    | Logwithquotes "Stage 2:"
    | If
        Isalphabetic
        To "Text is alphabetic."
        To "Text is not alphabetic."
    | Log

    START TEXT Logwithquotes TEXT:Textprefix
        | Addright "\""
        | Addleft "\""
        | Addleft Textprefix
        | Log
        | To Input

        START TEXT Nothing
            | To Input
            | To Input
            | To Input
            | To Input

    START TEXT Nothing
        | To Input
        | To Input
        | To Input
        | To Input

