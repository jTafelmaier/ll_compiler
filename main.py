

from src.compiler import compiler_ll_to_python




def main():

    # TODO repeat for all source files in any subdirectories

    with open("documentation/example.ll", "r", encoding="utf-8") as file_ll:
        text_ll = file_ll \
            .read()

    text_python_main = compiler_ll_to_python.get_text_python(text_ll)

    with open("documentation/example.py", "w", encoding="utf-8") as file_python:
        file_python \
            .write(text_python_main)

    import documentation.example as example

    example.nonpython_Main("example input")

    return None


if __name__ == "__main__":
    main()

