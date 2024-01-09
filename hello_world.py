

from built_in_functions import *



def main():

    def ll_to_text_rev(
        this):

        return ll_to_text_reversed(this)

    text_hello = "Hello"

    ll_print(ll_to_text_append(ll_to_text_reversed(ll_to_text_rev(ll_to_text_append(ll_to_text_uppercase(text_hello), " World"))), "!"))

    return None


if __name__ == "__main__":
    main()

