

import typing




def ll_prepend(
    text_input:str,
    text_to_prepend:str):

    return text_to_prepend \
        + text_input


def ll_append(
    text_input:str,
    text_to_append:str):

    return text_input \
        + text_to_append


def ll_reversed(
    text_input:str):

    return text_input \
        [::-1]


def ll_uppercase(
    text_input:str):

    return text_input \
        .upper()


def ll_print(
    text_input:str):

    print(text_input)


def ll_map(
    list_items:typing.List,
    function:typing.Callable[[typing.Any], typing.Any]):

    return list(
            map(
                function,
                list_items))


def ll_joined(
    list_texts_input:typing.List[str],
    text_join:str):

    return text_join \
        .join(list_texts_input)

