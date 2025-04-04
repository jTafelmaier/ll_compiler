

import typing




def get_text_indented_one_level(
    text:str):

    def get_text_line_indented(
        text_line:str):

        if text_line == "":
            return text_line

        return "    " \
            + text_line

    return "\n" \
        .join(
            map(
                get_text_line_indented,
                text \
                    .split("\n")))


def get_iterator_lists_pairs_lines_grouped_by_and_remove_indentation(
    iterable_pairs_lines:typing.Iterable[typing.Tuple[int, str]]):

    def get_iterator_reversed_texts_grouped_by_indentation():

        iterator_reversed_pairs_lines = reversed(list(iterable_pairs_lines))

        list_pairs_lines_block = []

        # TODO test further
        bool_in_block = False

        for pair_line in iterator_reversed_pairs_lines:

            index_line, \
            text_line = pair_line

            # TODO refactor
            if text_line.startswith("    "):
                bool_in_block = True

                list_pairs_lines_block \
                    .append((
                        index_line,
                        text_line \
                            [4:]))
            else:
                list_pairs_lines_block \
                    .append(pair_line)

                if text_line != "":
                    bool_in_block = False

                if not bool_in_block:
                    yield list(reversed(list_pairs_lines_block))
                    list_pairs_lines_block = []

    return reversed(
            list(
                get_iterator_reversed_texts_grouped_by_indentation()))


def get_iterator_texts_grouped_by_and_remove_indentation(
    text:str):

    iterable_pairs_lines = enumerate(
            text \
                .split("\n"))

    return map(
            lambda list_pairs_lines: "\n"
                .join(
                    map(
                        lambda pair: pair[-1],
                        list_pairs_lines)),
            get_iterator_lists_pairs_lines_grouped_by_and_remove_indentation(iterable_pairs_lines))


def get_item_tokens(
    text:str):

    def get_list_tokens_line(
        pair_line:typing.Tuple[int, str]):

        index_line, \
        text_line = pair_line

        def get_iterator_tokens():

            bool_in_string = False

            character_last = "\n"

            list_characters_current = []

            # TODO test further
            for character in text_line:

                bool_token_terminated_here = False

                if not bool_in_string:
                    if character == "#":
                        return
                    if character == " ":
                        if character_last == " ":
                            raise Exception(
                                    "Line " \
                                        + str(index_line) \
                                        + ": Two consecutive whitespaces are not allowed.")
                        bool_token_terminated_here = True

                if character == "\"" and character_last != "\\":
                    bool_in_string = not bool_in_string
                    if not bool_in_string:
                        bool_token_terminated_here = True

                        list_characters_current \
                            .append(character)

                if bool_token_terminated_here:
                    yield "" \
                        .join(list_characters_current)

                    list_characters_current = []
                else:
                    list_characters_current \
                        .append(character)

                character_last = character

            if bool_in_string:
                raise Exception(
                        "Line " \
                            + str(index_line) \
                            + ": String not terminated.")

            if len(list_characters_current) > 0:
                yield "" \
                    .join(list_characters_current)

        return list(get_iterator_tokens())

    def get_list_or_dict_tokens_section(
        list_pairs_lines:typing.List[typing.Tuple[int, str]]):

        # TODO when list_pairs_lines is empty

        if len(list_pairs_lines) == 1:

            pair_line = list_pairs_lines \
                [0]

            index_line = pair_line \
                [0]

            return {
                "type": "terminal",
                "index_line": index_line,
                "list_tokens": get_list_tokens_line(pair_line)}

        return list(
                map(
                    get_list_or_dict_tokens_section,
                    get_iterator_lists_pairs_lines_grouped_by_and_remove_indentation(list_pairs_lines)))

    return get_list_or_dict_tokens_section(
            list(
                enumerate(
                    text \
                        .split("\n"))))


def get_tuple_partitions_list(
    list_items:typing.List,
    function_separate:typing.Callable[[typing.Any], bool]):

    list_partition = []

    list_separator = []

    iterator_texts = iter(list_items)

    for item in iterator_texts:
        if function_separate(item):
            list_separator \
                .append(item)
            break
        list_partition \
            .append(item)

    # TODO test further
    return (
        list_partition,
        list_separator,
        list(iterator_texts))

