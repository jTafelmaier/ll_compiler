



def to_text_custom text

    return this
        > to_text_append " c1"
        > to_text_append " c2"


set text_hello = "Hello"


set text_world = "World"


do text_hello
    > to_text_uppercase
    > to_text_append " "
    > to_text_append text_world
    > to_text_custom
    > to_text_reversed
    > to_text_reversed
    > to_text_append "!"
    > print

