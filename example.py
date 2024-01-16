

from built_in_functions import *




def main():

    ll_ListTexts = [
        "Hello",
        "World"]

    ll_print(
        ll_append(
            ll_joined(
                ll_map(
                    ll_ListTexts,
                    lambda ll_Input: ll_uppercase(
                        ll_Input)),
                ", "),
            "!"))

    return None


if __name__ == "__main__":
    main()

