

from src.compiler.reader_ll import m_read_ll
from src.compiler.writer_python import m_write_python




def main():

    with open("example.ll", "r", encoding="utf-8") as file_ll:
        text_ll = file_ll \
            .read()

    dict_data = m_read_ll.get_dict_data_parsed_ll(text_ll)

    text_python_main = m_write_python.get_text_python_main(dict_data)

    with open("example.py", "w", encoding="utf-8") as file_python:
        file_python \
            .write(text_python_main)

    return None


if __name__ == "__main__":
    main()

