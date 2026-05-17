

import typing




if __name__ == "__main__":

    def get_average(
        list_ints:typing.List[int]):

        return float(sum(list_ints)) / len(list_ints)

    print(get_average([len(text) for text in "Test, Hello, World".split(", ") if text.isalpha()]))

