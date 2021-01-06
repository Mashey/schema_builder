import json
from schema_builder.builder_ddl import open_ddl_file, clean_data
from schema_builder.builder_table_list import parse_formatted_table

__version__ = '0.1.0'


def build_json_schema(source_type, file=None, data=None, table=None):
    if source_type == 'ddl':
        return schema_from_ddl(file)
    elif source_type == 'table':
        return schema_from_table(data, table)
    else:
        return "Please enter a valid source type [ddl, table]."


def create_table_dict(data):
    table_dict = {}

    for row in data:
        data_type = find_data_type(row[1])
        table_dict[row[0]] = data_type

    return table_dict


def find_data_type(data):
    # Idea :: use data_types in place of an if/elif chain to return the data type
    # data_types = {
    #     'INT': {"type": ["integer", "null"]},
    #     'BIGINT': {"type": ["integer", "null"]},
    #     'DECIMAL': {"type": ["number", "null"]},
    #     'VARCHAR': {"type": ["string", "null"]},
    #     'TIMESTAMP': {"type": ["string", "null"]}
    # }

    if 'INT' in data:
        return {"type": ["integer", "null"]}
    elif 'BIGINT' in data:
        return {"type": ["integer", "null"]}
    elif 'DECIMAL' in data:
        return {"type": ["number", "null"]}
    elif 'VARCHAR' in data:
        return {"type": ["string", "null"]}
    elif 'TIMESTAMP' in data:
        return {"type": ["string", "null"]}


def create_json_schema_dict(data):
    json_schema = {
        "type": ["object", "null"],
        "properties": data
    }

    return json_schema


def create_json_schema_file(data, table_name):
    json_schema = json.dumps(data, indent=4)

    with open(f"./schema_builder/schemas/{table_name}_schema.json", "w") as schema:
        schema.write(json_schema)

    return f"{table_name}_schema.json successfully created."


def schema_from_ddl(file):
    if file == None:
        return "Please enter a valid file path."

    raw_table_data = open_ddl_file(file)
    table_name, clean_table_data = clean_data(raw_table_data)
    table_dict = create_table_dict(clean_table_data)
    json_schema_dict = create_json_schema_dict(table_dict)

    return create_json_schema_file(json_schema_dict, table_name)


def schema_from_table(data, table):
    if data == None:
        return "Please provide data from a SQL DESCRIBE FORMATTED query."

    clean_table_data = parse_formatted_table(data)
    table_dict = create_table_dict(clean_table_data)
    json_schema_dict = create_json_schema_dict(table_dict)

    return create_json_schema_file(json_schema_dict, table)

