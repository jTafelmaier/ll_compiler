

import typing




if __name__ == "__main__":

    def get_average_length(
        list_texts:typing.List[str]):

        list_lengths = [len(text) for text in list_texts]

        return float(sum(list_lengths)) / len(list_lengths)

    print(get_average_length("Test, Hello, World".split(", ")))

