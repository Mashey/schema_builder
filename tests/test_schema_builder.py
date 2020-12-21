from schema_builder import *

def test_schema_type():
    assert schema_type(10) == "number"
    assert schema_type(10.5) == "number"

    assert schema_type(True) == 'boolean'
    assert schema_type(False) == 'boolean'

    assert schema_type({ "hello": "world" }) == 'object'
    assert schema_type({}) == 'object'

    assert schema_type(["hola", "mundo"]) == 'array'
    assert schema_type([1, 2, 3]) == 'array'
    assert schema_type([]) == 'array'

    assert schema_type("hello") == 'string'
