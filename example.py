

from built_in_functions import *




def main():

    def ll_applyTwoFunctionsReversed(
        ll_Input,
        ll_Function2,
        ll_Function1):

        def ll_doNothing(
            ll_Input,
            ll__):

            return ll_Input

        return ll_Function2(
            ll_Function1(
                ll_doNothing(
                    ll_Input,
                    None)))

    def ll_prepend(
        ll_Input,
        ll_Text):

        return ll_append(
            ll_Text,
            ll_Input)

    ll_ListTexts = [
        "Hello",
        "World"]

    ll_print(
        ll_applyTwoFunctionsReversed(
            ll_prepend(
                ll_joined(
                    ll_map(
                        ll_ListTexts,
                        lambda ll_Input: ll_uppercase(
                            ll_Input)),
                    " "),
                "I say: "),
            lambda ll_Input: ll_reversed(
                ll_Input),
            lambda ll_Input: ll_reversed(
                ll_Input)))

    return None


if __name__ == "__main__":
    main()

