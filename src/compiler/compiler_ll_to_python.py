

import json
import typing

from src.auxiliary import m_common_functions
from src.compiler import m_read_ll
from src.compiler import m_write_python




def get_text_python(
    text_ll:str):

    def save_json(
        name_file:str,
        item_json:typing.Union[typing.Dict, typing.List]):

        with open(name_file, "w", encoding="utf-8") as file_json:
            file_json \
                .write(json.dumps(
                    obj=item_json,
                    indent=4,
                    ensure_ascii=False))

    item_blocks = m_common_functions.get_item_tokens(text_ll)

    # save_json(
    #         name_file="ll_tokens.json",
    #         item_json=item_blocks)

    dict_data = m_read_ll.get_dict_data_parsed_ll(item_blocks)

    # save_json(
    #         name_file="ll_data.json",
    #         item_json=dict_data)

    return m_write_python.get_text_python_main(dict_data)

