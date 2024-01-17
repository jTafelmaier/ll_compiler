



ListTexts = [
        "hello",
        "_",
        ";;",
        "world",
        "1Error"]


ListTexts
    > retainIf isAlphabetic
    > map titlecase
    > joined ", "
    > append "!"
    > print

