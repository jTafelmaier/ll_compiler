

from src.compiler import m_compile




def main():

    with open("example.ll", "r", encoding="utf-8") as file_ll:
        text_ll = file_ll \
            .read()

    text_python_main = m_compile.get_text_python_main(text_ll)

    with open("example.py", "w", encoding="utf-8") as file_python:
        file_python \
            .write(text_python_main)

    return None


if __name__ == "__main__":
    main()

