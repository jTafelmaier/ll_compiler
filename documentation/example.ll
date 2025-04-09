



START TEXT Main
    | To "Adam Cain, Eve Abel, Delta 02"
    | Split ", "
    | Filter [Seq [Seq [Split " "] [Join ""]] Isalphabetic]
    | Map [PERSON Unchanged [Addright "@protonmail.com"] [To 20]]
    + $listData
    | Log
    | Map Emailcorrected
    | Join ", "
    | Addleft "Emails: "
    | Log
    | To $listData
    | Map name
    | Join ", "
    | Addleft "Names: "
    | Log

    CLASS PERSON
        L TEXT:name
        L TEXT:email
        L INTEGER:age

    START PERSON Emailcorrected
        | email
        | Map [If [Equalsint " "] [To "_"] Unchanged]
        | Join ""

