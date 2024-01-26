

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

        # TODO test
        for pair_line in iterator_reversed_pairs_lines:

            index_line, \
            text_line = pair_line

            if text_line == "" and len(list_pairs_lines_block) == 0:
                continue

            # TODO refactor
            if text_line.startswith("    "):
                list_pairs_lines_block \
                    .append((
                        index_line,
                        text_line \
                            [4:]))
            else:
                list_pairs_lines_block \
                    .append(pair_line)

                if text_line != "":
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
                .join(map(
                    lambda pair: pair[-1],
                    list_pairs_lines)),
            get_iterator_lists_pairs_lines_grouped_by_and_remove_indentation(iterable_pairs_lines))


def get_dict_tokens(
    text:str):

    def get_list_tokens_line(
        pair_line:typing.Tuple[int, str]):

        index_line, \
        text_line = pair_line

        def get_iterator_tokens():

            in_string = False

            character_last = "\n"

            list_characters_current = []

            # TODO test
            # TODO type and list brackets
            for character in text_line:

                if character == " " and not in_string:
                    if character_last == " ":
                        raise Exception(
                                "Line " \
                                    + str(index_line) \
                                    + ": Two consecutive whitespaces are not allowed.")

                    yield "" \
                        .join(list_characters_current)

                    list_characters_current = []
                else:
                    list_characters_current \
                        .append(character)

                if character == "\"" and character_last != "\\":
                    in_string = not in_string
                    if not in_string:
                        yield "" \
                            .join(list_characters_current)

                        list_characters_current = []

                character_last = character

            if len(list_characters_current) > 0:
                yield "" \
                    .join(list_characters_current)

            if in_string:
                raise Exception(
                        "Line " \
                            + str(index_line) \
                            + ": String not terminated.")

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

        # TODO test
        return list(
                map(
                    get_list_or_dict_tokens_section,
                    get_iterator_lists_pairs_lines_grouped_by_and_remove_indentation(list_pairs_lines)))

    list_or_dict_tokens_blocks = get_list_or_dict_tokens_section(
            list(
                enumerate(
                    text \
                        .split("\n"))))

    return {
        "tokens": list_or_dict_tokens_blocks}


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

    # TODO test
    return (
        list_partition,
        list_separator,
        list(iterator_texts))

