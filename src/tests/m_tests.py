

from src.compiler import m_compile




def test_compiler():

    list_tests = [
        (
            """Nested Function call""",
            """\n"Hello World 1"\n    > text_reverse\n    > print\n""",
            """\n\n#include <stdio.h>\n\n\n\n\nint main() {\n\n    printf(strrev("Hello World 1"));\n\n    return 0;\n}\n\n"""),
        (
            """Multiple statements""",
            """\n\n\n\n"Hello World 1"\n    > print\n\n"Hello World 2"\n    > print\n\n""",
            """\n\n#include <stdio.h>\n\n\n\n\nint main() {\n\n    printf("Hello World 1");\n\n    printf("Hello World 2");\n\n    return 0;\n}\n\n""")]

    for text_name_test, text_ll, text_c_target in list_tests:

        text_c_compiled = m_compile.get_text_c(text_ll)

        if text_c_compiled == text_c_target:

            print(
                "SUCCESSFUL: " \
                    + text_name_test)

            continue

        print(
            "ERROR: " \
                + text_name_test \
                + "\nTARGET:   " \
                + text_c_target \
                + "\nCOMPILED: " \
                + text_c_compiled)

        break

    return None

