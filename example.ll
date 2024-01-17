


def BOOL true
    NOTHING _

    return True


ListTexts = [
        "hello",
        "world"]


ListTexts
    > filter true None
    > map titlecase
    > joined ", "
    > append "!"
    > print

