



START TEXT Main
    | To "Adam Cain, Eve Abel, Delta 02"
    | Split ", "
    | Filter [Seq [Replace " " ""] Isalphabetic]
    | Map [PERSON Unchanged Getemail [To 20]]
    + listdata
    | Logdataofperson .email "Emails"
    | Logdataofperson .name "Names"

    CLASS PERSON
        - TEXT name
        - TEXT email
        - INTEGER age

    START TEXT Getemail
        | Replace " " "_"
        | Addright "@protonmail.com"

    START [LIST PERSON] Logdataofperson
        - [FUNCTION PERSON TEXT] getattribute
        - TEXT title
        | Map getattribute
        | Join "\n  "
        | Addleft ":\n  "
        | Addleft title
        | Addleft "\n"
        | Log
        | To input

