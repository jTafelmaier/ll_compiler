

from src.compiler import m_compile




def main():

    with open("hello_world.ll", "r", encoding="utf-8") as file_ll:
        text_ll = file_ll \
            .read()

    with open("hello_world.py", "w", encoding="utf-8") as file_python:
        file_python \
            .write(m_compile.get_text_python_main(text_ll))

    return None


if __name__ == "__main__":
    main()

