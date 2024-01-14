

from built_in_functions import *




def main():

    def ll_applyFunction(
        ll_Input,
        ll_Function):

        return ll_Function(
            ll_Input)

    def ll_applyTwoFunctionsReversed(
        ll_Input,
        ll_Function2,
        ll_Function1):

        return ll_Function2(
            ll_Function1(
                ll_Input))

    def ll_prepend(
        ll_Input,
        ll_Text):

        return ll_append(
            ll_Text,
            ll_Input)

    ll_print(
        ll_applyTwoFunctionsReversed(
            ll_applyFunction(
                ll_applyFunction(
                    ll_applyFunction(
                        ll_applyTwoFunctionsReversed(
                            "Hello",
                            lambda ll_Input: ll_append(
                                ll_Input,
                                "!"),
                            lambda ll_Input: ll_append(
                                ll_Input,
                                " World")),
                        lambda ll_Input: ll_prepend(
                            ll_Input,
                            "I say: ")),
                    ll_reversed),
                ll_reversed),
            ll_reversed,
            ll_reversed))

    return None


if __name__ == "__main__":
    main()

