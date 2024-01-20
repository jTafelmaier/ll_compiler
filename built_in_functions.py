

import typing




def nonpython_toText(
    int_input:int):

    return str(int_input)


def nonpython_isAlphabetic(
    text_input:str):

    return text_input \
        .isalpha()


def nonpython_prepend(
    text_input:str,
    text_to_prepend:str):

    return text_to_prepend \
        + text_input


def nonpython_append(
    text_input:str,
    text_to_append:str):

    return text_input \
        + text_to_append


def nonpython_reversed(
    text_input:str):

    return text_input \
        [::-1]


def nonpython_lowercase(
    text_input:str):

    return text_input \
        .lower()


def nonpython_uppercase(
    text_input:str):

    return text_input \
        .upper()


def nonpython_titlecase(
    text_input:str):

    return text_input \
        .title()


def nonpython_splitOn(
    text_input:str,
    text_separator:str):

    return text_input \
        .split(text_separator)


def nonpython_print(
    text_input:str):

    print(text_input)


def nonpython_map(
    list_items:typing.List,
    function:typing.Callable[[typing.Any], typing.Any]):

    return list(
            map(
                function,
                list_items))


def nonpython_retainIf(
    list_items:typing.List,
    function:typing.Callable[[typing.Any], bool]):

    return list(
            filter(
                function,
                list_items))


def nonpython_joined(
    list_texts_input:typing.List[str],
    text_join:str):

    return text_join \
        .join(list_texts_input)

