



START TEXT Main
    | To "Test, Hello, World"
    | Split ", "
    | Map Length
    | Getaverage
    | Log

    START LIST[INTEGER] Getaverage
        | Length
        + countItems
        | To input
        | Sum
        | Dividefloat countItems

