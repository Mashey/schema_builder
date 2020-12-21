from pprint import pprint

TYPES = {
    int: 'number',
    float: 'number',
    bool: 'boolean',
    dict: 'object',
    list: 'array',
    str: 'string'
}

def to_json_type(input_type):
    return TYPES.get(input_type, 'null')

def create_json_instance(key, value):
    instance = {}
    value_type = type(value)
    instance[key] = {
        "type": to_json_type(value_type)
    }
    return instance

def create_json_definition(def_name, properties):
    definition = { "type": ['null', 'object'] }
    instances = {}
    for key, value in properties.items():
        instances.update(create_json_instance(key, value))
    definition['properties'] = instances

    return { def_name: definition }