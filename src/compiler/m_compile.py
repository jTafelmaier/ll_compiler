



def compile_source():

    with open("hello_world.ll", "r", encoding="utf-8") as file_ll:
        text_ll = file_ll \
            .read()

    text_c = ""

    with open("hello_world.c", "w", encoding="utf-8") as file_c:
        file_c \
            .write(text_c)

    return None

