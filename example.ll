


def ANYTHING true

    return True


ListTexts = [
        "hello",
        "world"]


ListTexts
    > retainIf true
    > map titlecase
    > joined ", "
    > append "!"
    > print

