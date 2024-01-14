

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
            ll_uppercase(
                ll_applyTwoFunctions(
                    "Hello",
                    lambda Input: ll_append(
                        Input,
                        " World"),
                    lambda Input: ll_append(
                        Input,
                        "!"))),
            lambda Input: ll_reversed(
                Input),
            lambda Input: ll_reversed(
                Input)))

    return None


if __name__ == "__main__":
    main()

