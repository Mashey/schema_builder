import pytest

from schema_builder import *

def to_json_type_test_inputs():
    return [
        (int, 'number'),
        (float, 'number'),
        (dict, 'object'),
        (list, 'array'),
        (str, 'string'),
        (None, 'null')
    ]

@pytest.mark.parametrize("input_type,expected", to_json_type_test_inputs())
def test_to_json_type(input_type, expected):
    assert to_json_type(input_type) == expected

def create_json_instance_test_inputs():
    return [
        ("id", 10, {"id": {"type": "number"}}),
        ("amount", 10.5, {"amount": {"type": "number"}}),
        ("is_active", True, {"is_active": {"type": "boolean"}}),
        ("name", "Bob", {"name": {"type": "string"}})
    ]

@pytest.mark.parametrize("key,value,expected", create_json_instance_test_inputs())
def test_create_json_instance(key, value, expected):
    assert create_json_instance(key, value) == expected

def create_json_definition_test_inputs():
    return [
        (
            "location",
            {"address": "123 Main St", "city": "Boulder", "state": "CO"},
            {
                "location": {
                    "type": ["null", "object"],
                    "properties": {
                        "address": {
                            "type": 'string'
                        },
                        "city": {
                            "type": 'string'
                        },
                        "state": {
                            "type": 'string'
                        }
                    }
                }
            }
        )
    ]

@pytest.mark.parametrize("def_name,properties,expected", create_json_definition_test_inputs())
def test_create_json_definition(def_name, properties, expected):
    assert create_json_definition(def_name, properties) == expected
