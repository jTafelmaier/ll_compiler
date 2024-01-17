

from built_in_functions import *




def main():

    def ll_true(
        ll_Input,
        ll__):

        return True

    ll_ListTexts = [
        "hello",
        "world"]

    ll_print(
        ll_append(
            ll_joined(
                ll_map(
                    ll_filter(
                        ll_ListTexts,
                        lambda ll_Input: ll_true(
                            ll_Input,
                            None)),
                    lambda ll_Input: ll_titlecase(
                        ll_Input)),
                ", "),
            "!"))

    return None


if __name__ == "__main__":
    main()

