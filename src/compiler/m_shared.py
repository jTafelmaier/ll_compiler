



class Object_variable:

    KEY_TEXT_CATEGORY = "category"


class Comment:

    KEY_TEXT = "text"


class Function_definition:

    KEY_TEXT_NAME_FUNCTION = "name_function"
    KEY_TEXT_TYPE_INPUT = "type_input"
    KEY_ARRAY_DICTS_ARGUMENTS = "arguments"
    KEY_ARRAY_DICTS_INNER_FUNCTION_DEFINITIONS = "inner_function_definitions"
    KEY_ARRAY_DICTS_OPERATIONS = "operations"

    class Argument:

        KEY_TEXT_NAME = "name_argument"
        KEY_TEXT_TYPE = "type"


class Function_reference:

    KEY_NAME_FUNCTION = "name_function"
    KEY_ARRAY_OBJECTS_ARGUMENTS = "arguments"


class Memory_write:

    KEY_TEXT_KEY_MEMORY = "key_memory_write"


class Memory_read:

    KEY_TEXT_KEY_MEMORY = "key_memory_read"


class Literal:

    KEY_TEXT_VALUE = "value"

