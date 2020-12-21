def schema_type(value):
    value_type = type(value)
    types = {
        int: 'number',
        float: 'number',
        bool: 'boolean',
        dict: 'object',
        list: 'array',
        str: 'string'
    }
    return types.get(value_type, 'null')
