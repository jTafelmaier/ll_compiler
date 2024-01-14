

from built_in_functions import *




def main():

    def ll_applyFunction(
        Input,
        ll_Function):

        return ll_Function(
            Input)

    def ll_applyTwoFunctionsReversed(
        Input,
        ll_Function2,
        ll_Function1):

        return ll_Function2(
            ll_Function1(
                Input))

    ll_print(
        ll_applyTwoFunctionsReversed(
            ll_applyFunction(
                ll_applyTwoFunctionsReversed(
                    "Hello",
                    lambda Input: ll_append(
                        Input,
                        "!"),
                    lambda Input: ll_append(
                        Input,
                        " World")),
                lambda Input: ll_append(
                    Input,
                    " c1")),
            lambda Input: ll_reversed(
                Input),
            lambda Input: ll_reversed(
                Input)))

    return None


if __name__ == "__main__":
    main()

