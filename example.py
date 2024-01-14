

from built_in_functions import *




def main():

    def ll_applyTwoFunctions(
        Input,
        ll_Function1,
        ll_Function2):

        return ll_Function2(
            ll_Function1(
                Input))

    ll_print(
        ll_applyTwoFunctions(
            ll_applyTwoFunctions(
                ll_uppercase(
                    "Hello World!"),
                ll_reversed,
                ll_reversed),
            lambda Input: ll_append(Input, " c1"),
            lambda Input: ll_append(Input, " c2")))

    return None


if __name__ == "__main__":
    main()

