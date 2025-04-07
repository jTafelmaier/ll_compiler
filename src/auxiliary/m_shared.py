



KEY_CATEGORY_LITERAL = "literal"
KEY_CATEGORY_FUNCTION = "function"
KEY_CATEGORY_MEMORY_READ = "memory_read"
KEY_CATEGORY_MEMORY_WRITE = "memory_write"
KEY_CATEGORY_DEFINITION_CLASS = "definition_class"
KEY_CATEGORY_DEFINITION_FUNCTION = "definition_function"


class Object_variable:

    KEY_TEXT_CATEGORY = "category"


class Argument:

    KEY_TEXT_NAME = "name_argument"
    KEY_TEXT_TYPE = "type"


class Definition_class:

    KEY_TEXT_NAME_CLASS = "name_class"
    KEY_TEXT_TYPE_CLASS = "type_class"
    KEY_ARRAY_DICTS_MEMBERS = "members"


class Definition_function:

    KEY_TEXT_NAME_FUNCTION = "name_function"
    KEY_TEXT_TYPE_INPUT = "type_input"
    KEY_ARRAY_DICTS_ARGUMENTS = "arguments"
    KEY_ARRAY_DICTS_OPERATIONS = "operations"
    KEY_ARRAY_DICTS_INNER_DEFINITIONS = "inner_definitions"


class Function_reference:

    KEY_NAME_FUNCTION = "name_function"
    KEY_ARRAY_OBJECTS_ARGUMENTS = "arguments"


class Memory_write:

    KEY_TEXT_KEY_MEMORY = "key_memory_write"


class Memory_read:

    KEY_TEXT_KEY_MEMORY = "key_memory_read"


class Literal:

    KEY_TEXT_VALUE = "value"

