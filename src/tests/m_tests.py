

from src.compiler import m_compile




def test_compiler():

    list_tests = [
        (
            """Nested Function call""",
            """\n\n\n\n"Hello World 1"\n    > text_reverse\n    > print\n\n""",
            """\n\n#include <stdio.h>\n\n\n\n\nint main(void) {\n\n    printf(strrev("Hello World 1"));\n\n    return 0;\n}\n\n"""),
        (
            """Multiple statements""",
            """\n\n\n\n"Hello World 1"\n    > print\n\n"Hello World 2"\n    > print\n\n""",
            """\n\n#include <stdio.h>\n\n\n\n\nint main(void) {\n\n    printf("Hello World 1");\n\n    printf("Hello World 2");\n\n    return 0;\n}\n\n"""),
        (
            """Function argument""",
            """\n\n\n\n"You entered: %d"\n    > print [5]\n\n""",
            """\n\n#include <stdio.h>\n\n\n\n\nint main(void) {\n\n    printf("You entered: %d", 5);\n\n    return 0;\n}\n\n"""),
        (
            """Variable assignment""",
            """\n\n\n\ntext_hello_world = "Hello World"\n\ntext_hello_world\n    > text_reverse\n    > print\n\n""",
            """\n\n#include <stdio.h>\n\n\n\n\nint main(void) {\n\n    char text_hello_world[] = "Hello World";\n\n    printf(strrev(text_hello_world));\n\n    return 0;\n}\n\n"""),
        (
            """Integer assignment""",
            """\n\n\ninteger_test = 15\n\n"test: %d"\n    > print [integer_test]\n\n""",
            """\n\n#include <stdio.h>\n\n\n\n\nint main(void) {\n\n    int integer_test = 15;\n\n    printf("test: %d", integer_test);\n\n    return 0;\n}\n\n""")]

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

