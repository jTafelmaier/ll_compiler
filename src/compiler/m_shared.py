



class Object_variable:

    KEY_TEXT_CATEGORY = "category"


class Comment:

    KEY_TEXT = "text"


class Expression_return:

    KEY_OBJECT = "expression"


class Function_definition:

    KEY_TEXT_NAME_FUNCTION = "name_function_def"
    KEY_TEXT_TYPE_INPUT = "type_input"
    KEY_ARRAY_OBJECTS_ARGUMENTS = "arguments_def"
    KEY_ARRAY_OBJECTS_BODY = "body"

    class Argument:

        KEY_TEXT_NAME = "name_argument_def"
        KEY_TEXT_TYPE = "type"


class Function_reference:

    KEY_NAME_FUNCTION = "name_function"
    KEY_ARRAY_OBJECTS_ARGUMENTS = "arguments"


class Memory_allocation:

    KEY_TEXT_KEY_MEMORY = "key_memory_allocation"
    KEY_OBJECT_CONTENT = "expression"


class Memory_read:

    KEY_TEXT_KEY_MEMORY = "key_memory_read"


class Literal:

    KEY_TEXT_VALUE = "value"


class Expression:

    KEY_OBJECT_INITIAL = "initial"
    KEY_ARRAY_OBJECTS_FUNCTION_CALLS = "function_calls"




