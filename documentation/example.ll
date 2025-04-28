



START TEXT Main
    | To "Adam Cain, Eve Abel, Delta 02"
    | Split ", "
    | Filter [Unite [Replace " " ""] Isalphabetic]
    | Map [PERSON Unchanged Getemail [To 20]]
    + listdata
    | Filter [Unite .name [Equalsint "Adam Cain"]]
    | Logdataofperson .email "Emails"
    | To listdata
    | Logdataofperson .name "Names"

    CLASS PERSON
        - TEXT name
        - TEXT email
        - INTEGER age

    START TEXT Getemail
        | Replace " " "_"
        | Addright "@protonmail.com"

    START [LIST PERSON] Logdataofperson
        - [FUNCTION PERSON TEXT] Function1
        - TEXT title
        | Map Function1
        | Join "\n  "
        | Addleft ":\n  "
        | Addleft title
        | Addleft "\n"
        | Log
        | To input

