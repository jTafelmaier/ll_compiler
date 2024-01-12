

from built_in_functions import *




def main():

    def ll_appendTwice(
        input,
        text):

        return ll_append(ll_append(input, text), text)

    world = ll_uppercase(ll_append("World", "!"))

    ll_print(ll_appendTwice(ll_append(ll_uppercase(ll_append("Hello", " ")), world), " c"))

    return None


if __name__ == "__main__":
    main()

