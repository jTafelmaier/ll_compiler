



START TEXT Main
    | To "Adam Cain, Eve Abel, Delta 02"
    | Split ", "
    | Filter [Seq [Replacesubtext " " ""] Isalphabetic]
    | Map [PERSON Unchanged Getemail [To 20]]
    + :listData
    | Logdata email "Emails"
    | Logdata name "Names"

    CLASS PERSON
        - TEXT name
        - TEXT email
        - INTEGER age

    START TEXT Getemail
        | Map [If [Equalsint " "] [To "_"] Unchanged]
        | Join ""
        | Addright "@protonmail.com"

    START [LIST PERSON] Logdata
        - [FUNCTION PERSON TEXT] :getattribute
        - TEXT :title
        | Map :getattribute
        | Join "\n  "
        | Addleft ":\n  "
        | Addleft :title
        | Addleft "\n"
        | Log
        | To :input

