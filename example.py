

from built_in_functions import *




def main():

    ll_ListTexts = [
        "hello",
        "_",
        ";;",
        "world",
        "1Error"]

    ll_print(
        ll_append(
            ll_joined(
                ll_map(
                    ll_retainIf(
                        ll_ListTexts,
                        lambda ll_Input: ll_isAlphabetic(
                            ll_Input)),
                    lambda ll_Input: ll_titlecase(
                        ll_Input)),
                ", "),
            "!"))

    return None


if __name__ == "__main__":
    main()

