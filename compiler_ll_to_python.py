

import json

from src.auxiliary import m_common_functions
from src.compiler.reader_ll import m_read_ll
from src.compiler.writer_python import m_write_python




def main():

    with open("example.ll", "r", encoding="utf-8") as file_ll:
        text_ll = file_ll \
            .read()

    item_blocks = m_common_functions.get_item_tokens(text_ll)

    with open("tokens.json", "w", encoding="utf-8") as file_json:
        file_json \
            .write(json.dumps(item_blocks, indent=4, ensure_ascii=False))

    dict_data = m_read_ll.get_dict_data_parsed_ll(item_blocks)

    text_python_main = m_write_python.get_text_python_main(dict_data)

    with open("example.py", "w", encoding="utf-8") as file_python:
        file_python \
            .write(text_python_main)

    return None


if __name__ == "__main__":
    main()

