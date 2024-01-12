

from built_in_functions import *



def main():

    def ll_appendTwice(
        input,
        text):

        return ll_append(ll_append(input, text), text)

    hello = "Hello"

    world = "World"

    ll_print(ll_append(ll_reversed(ll_reversed(ll_appendTwice(ll_append(ll_append(ll_uppercase(hello), " "), world), " c"))), "!"))

    return None


if __name__ == "__main__":
    main()

