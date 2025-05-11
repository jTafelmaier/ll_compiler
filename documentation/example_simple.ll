



FUNCTION TEXT Main
    | To "Test, Hello, World, 00"
    | Split ", "
    | Filter Isalphabetic
    | Map Length
    | Getaverage
    | Log

    FUNCTION LIST[INTEGER] Getaverage
        | Length
        + countItems
        | To input
        | Sum
        | Dividefloat countItems

