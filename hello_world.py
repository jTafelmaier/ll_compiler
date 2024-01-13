

from built_in_functions import *




def main():

    def ll_appendTwoTexts(
        input,
        text1,
        text2,
        text3):

        return ll_append(ll_append(ll_append(input, text1), text2), text3)

    world = ll_uppercase(ll_append("World", "!"))

    ll_print(ll_appendTwoTexts(ll_append(ll_uppercase(ll_append("Hello", " ")), world), " c1", " c2", " c3"))

    return None


if __name__ == "__main__":
    main()

