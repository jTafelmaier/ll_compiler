



START TEXT Main
    | To "Test, Hello, World"
    | Split ", "
    | Getaveragelength
    | Log

    START LIST[TEXT] Getaveragelength
        | Length
        + countItems
        | To input
        | Map Length
        | Sum
        | Dividefloat countItems

