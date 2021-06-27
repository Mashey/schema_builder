import json
import os
import logging


def create_ddl_dict(data):
    table_dict = {}
    table_columns = data[1]

    for row in table_columns:
        data_type = find_ddl_data_type(row[1])
        json_schema_type = set_data_type(data_type)
        table_dict[row[0]] = json_schema_type

    return table_dict


def find_ddl_data_type(data) -> str:
    lowercase_data = data.lower()
    data_type = ""

    if "int" in lowercase_data:
        data_type = "int"
    elif "bigint" in lowercase_data:
        data_type = "int"
    elif "decimal" in lowercase_data:
        data_type = "float"
    elif "varchar" in lowercase_data:
        data_type = "string"
    elif "char" in lowercase_data:
        data_type = "string"
    elif "string" in lowercase_data:
        data_type = "string"
    elif "timestamp" in lowercase_data:
        data_type = "string"

    return data_type


def set_data_type(data_type: str) -> object:
    types = {
        "int": {"type": ["integer", "null"]},
        "float": {"type": ["number", "null"]},
        "string": {"type": ["string", "null"]},
        "dict": {"type": "object", "properties": {}},
        "array": {"type": "array"},
        "bool": {"type": "boolean"},
        "none": {"type": "null"},
    }
    current_type = types[data_type]

    return current_type


def create_json_schema_dict(data):
    json_schema = {"type": ["object", "null"], "properties": data}

    return json_schema


def create_json_schema_file(data, table_name):
    json_schema = json.dumps(data, indent=4)
    path = os.getcwd()

    try:
        os.mkdir(f"{path}/json_schemas")
    except FileExistsError:
        logging.warning("/json_schemas directory already exists.")

    with open(f"{path}/json_schemas/{table_name}_schema.json", "w") as schema:
        schema.write(json_schema)

    return f"{table_name}_schema.json created successfully."
