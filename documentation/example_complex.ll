



FUNCTION TEXT Main
    | To "Adam Cain, Eve Abel, Delta 02"
    | Split ", "
    | Filter Unite[Replace[" " ""] Isalphabetic]
    | Map PERSON[Unchanged Estimateemail Estimateage]
    + listdata
    | Log
    | Filter Unite[.name Equals["Adam Cain"]]
    | Logattribute .email "Emails"
    | To listdata
    | Logattribute .name "Names"

    CLASS PERSON
        - TEXT name
        - TEXT email
        - INTEGER age

    FUNCTION TEXT Estimateemail
        | Replace " " "_"
        | Addright "@protonmail.com"

    FUNCTION TEXT Estimateage
        | Length
        | Plus 10

    FUNCTION LIST[PERSON] Logattribute
        - FUNCTION[PERSON TEXT] Function1
        - TEXT title
        | Map Function1
        | Join "\n  "
        | Addleft ":\n  "
        | Addleft title
        | Addleft "\n"
        | Log
        | To input

