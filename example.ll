


def ANYTHING true

    return True


ListTexts = [
        "hello",
        "world"]


ListTexts
    > filter true
    > map titlecase
    > joined ", "
    > append "!"
    > print

