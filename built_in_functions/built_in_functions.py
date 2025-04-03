

import typing




def nonpython_unchanged(
    item_input:typing.Any):

    return item_input


def nonpython_to(
    item_input:typing.Any,
    item_other:typing.Any):

    return item_other


def nonpython_if(
    item_input:typing.Any,
    function_condition:typing.Callable[[typing.Any], bool],
    function_then:typing.Callable[[typing.Any], typing.Any],
    function_else:typing.Callable[[typing.Any], typing.Any]):

    if function_condition(item_input):
        return function_then(item_input)
    else:
        return function_else(item_input)


def nonpython_toText(
    int_input:int):

    return str(int_input)


def nonpython_plus(
    int_input:int,
    int_to_add:int):

    return int_input \
        + int_to_add


def nonpython_minus(
    int_input:int,
    int_arg:int):

    return int_input \
        - int_arg


def nonpython_isAlphabetic(
    text_input:str):

    return text_input \
        .isalpha()


def nonpython_prepend(
    text_input:str,
    text_to_add:str):

    return text_to_add \
        + text_input


def nonpython_add(
    text_input:str,
    text_to_append:str):

    return text_input \
        + text_to_append


def nonpython_reversed(
    text_input:str):

    return text_input \
        [::-1]


def nonpython_lower(
    text_input:str):

    return text_input \
        .lower()


def nonpython_upper(
    text_input:str):

    return text_input \
        .upper()


def nonpython_title(
    text_input:str):

    return text_input \
        .title()


def nonpython_split(
    text_input:str,
    text_separator:str):

    return text_input \
        .split(text_separator)


def nonpython_log(
    text_input:str):

    print(text_input)

    return text_input


def nonpython_logOther(
    text_input:str,
    text_other:str):

    print(text_other)

    return text_input


def nonpython_map(
    list_items:typing.List,
    function:typing.Callable[[typing.Any], typing.Any]):

    return list(
            map(
                function,
                list_items))


def nonpython_filter(
    list_items:typing.List,
    function:typing.Callable[[typing.Any], bool]):

    return list(
            filter(
                function,
                list_items))


def nonpython_join(
    list_texts_input:typing.List[str],
    text_join:str):

    return text_join \
        .join(list_texts_input)


def nonpython_length(
    list_input:typing.List):

    return len(list_input)


def nonpython_equalsInt(
    int_input:int,
    int_arg:int):

    return int_input \
        == int_arg

