

import typing




def nonpython_Unchanged(
    item_input:typing.Any):

    return item_input


def nonpython_To(
    item_input:typing.Any,
    item_other:typing.Any):

    return item_other


def nonpython_If(
    item_input:typing.Any,
    function_condition:typing.Callable[[typing.Any], bool],
    function_then:typing.Callable[[typing.Any], typing.Any],
    function_else:typing.Callable[[typing.Any], typing.Any]):

    if function_condition(item_input):
        return function_then(item_input)
    else:
        return function_else(item_input)


def nonpython_Totext(
    int_input:int):

    return str(int_input)


def nonpython_Plus(
    int_input:int,
    int_to_add:int):

    return int_input \
        + int_to_add


def nonpython_Minus(
    int_input:int,
    int_arg:int):

    return int_input \
        - int_arg


def nonpython_Isalphabetic(
    text_input:str):

    return text_input \
        .isalpha()


def nonpython_Addleft(
    text_input:str,
    text_to_add:str):

    return text_to_add \
        + text_input


def nonpython_Addright(
    text_input:str,
    text_to_append:str):

    return text_input \
        + text_to_append


def nonpython_Reversed(
    text_input:str):

    return text_input \
        [::-1]


def nonpython_Lowercase(
    text_input:str):

    return text_input \
        .lower()


def nonpython_Uppercase(
    text_input:str):

    return text_input \
        .upper()


def nonpython_Titlecase(
    text_input:str):

    return text_input \
        .title()


def nonpython_Split(
    text_input:str,
    text_separator:str):

    return text_input \
        .split(text_separator)


def nonpython_Log(
    text_input:str):

    print(text_input)

    return text_input


def nonpython_Logother(
    text_input:str,
    text_other:str):

    print(text_other)

    return text_input


def nonpython_Map(
    list_items:typing.List,
    function:typing.Callable[[typing.Any], typing.Any]):

    return list(
            map(
                function,
                list_items))


def nonpython_Filter(
    list_items:typing.List,
    function:typing.Callable[[typing.Any], bool]):

    return list(
            filter(
                function,
                list_items))


def nonpython_Join(
    list_texts_input:typing.List[str],
    text_join:str):

    return text_join \
        .join(list_texts_input)


def nonpython_Length(
    list_input:typing.List):

    return len(list_input)


def nonpython_Equalsint(
    int_input:int,
    int_arg:int):

    return int_input \
        == int_arg

