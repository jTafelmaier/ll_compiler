

from built_in_functions import *




def main():

    def ll_reverseTwice(
        Input,
        _):

        return ll_reversed(ll_reversed(Input))

    def ll_appendTwoTexts(
        Input,
        Text1,
        Text2):

        Text1Copy = ll_append(Text1, "")

        Text2Copy = ll_append(Text2, "")

        return ll_append(ll_append(Input, Text1Copy), Text2Copy)

    ll_print(ll_reverseTwice(ll_appendTwoTexts(ll_uppercase("Hello World!"), " c1", " c2"), None))

    return None


if __name__ == "__main__":
    main()

