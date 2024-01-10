

from built_in_functions import *



def main():

    def ll_toTextCustom(
        this):

        return ll_toTextAppend(ll_toTextAppend(this, " c1"), " c2")

    textHello = "Hello"

    textWorld = "World"

    ll_print(ll_toTextAppend(ll_toTextReversed(ll_toTextReversed(ll_toTextCustom(ll_toTextAppend(ll_toTextAppend(ll_toTextUppercase(textHello), " "), textWorld)))), "!"))

    return None


if __name__ == "__main__":
    main()

