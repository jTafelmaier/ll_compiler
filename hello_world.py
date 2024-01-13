

from built_in_functions import *




def main():

    def ll_appendTwoTexts(
        Input,
        Text1,
        Text2):

        Text3 = Text2

        return ll_append(ll_append(Input, Text1), Text3)

    World = ll_uppercase(ll_append("World", "!"))

    ll_print(ll_appendTwoTexts(ll_append(ll_uppercase(ll_append("Hello", " ")), World), " c1", " c2"))

    return None


if __name__ == "__main__":
    main()

