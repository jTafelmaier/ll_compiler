



def text to_text_rev

    return this
        > to_text_reversed


set text_hello = "Hello"


do text_hello
    > to_text_uppercase
    > to_text_append " World"
    > to_text_rev
    > to_text_reversed
    > to_text_append "!"
    > print

