

from src.compiler import m_compile




def test_compiler():

    list_tests = [
        (
            """Test 1""",
            """\n\n\ninteger_test = 15\n\n"test"\n    > print [integer_test]\n\n""",
            """\n\n\n\ndef main():\n\n    integer_test = 15\n\n    print("test", integer_test)\n\n    return None\n\n\nif __name__ == "__main__":\n    main()\n\n""")]

    for text_name_test, text_ll, text_python_target in list_tests:

        text_python_compiled = m_compile.get_text_python(text_ll)

        if text_python_compiled == text_python_target:

            print(
                "SUCCESSFUL: " \
                    + text_name_test)

            continue

        print(
            "ERROR: " \
                + text_name_test \
                + "\nTARGET:   " \
                + text_python_target \
                + "\nCOMPILED: " \
                + text_python_compiled)

        break

    return None

