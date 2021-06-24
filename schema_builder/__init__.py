import json
import os
import logging
from schema_builder.builder_ddl import open_ddl_file, clean_data
from schema_builder.builder_table_list import parse_formatted_table


def build_json_schema(source_type, file=None, data=None, table_name=None):
    if source_type == "ddl":
        return schema_from_ddl_file(file)
    if source_type == "table":
        return schema_from_table(data, table_name)
    return "Please enter a valid source type [ddl, table]."


def schema_from_ddl_file(file):
    if file is None:
        return "Please enter a valid file path."

    raw_table_data = open_ddl_file(file)
    clean_table_data = clean_data(raw_table_data)
    table_name = clean_table_data[0]
    table_dict = create_table_dict(clean_table_data)
    json_schema_dict = create_json_schema_dict(table_dict)

    return create_json_schema_file(json_schema_dict, table_name)


def schema_from_table(data, table_name):
    if data is None:
        return "Please provide data from a SQL DESCRIBE FORMATTED query."

    if table_name is None:
        return "Please provide a table name."

    clean_table_data = parse_formatted_table(data, table_name)
    table_dict = create_table_dict(clean_table_data)
    json_schema_dict = create_json_schema_dict(table_dict)

    return create_json_schema_file(json_schema_dict, table_name)


def schema_from_api():
    pass


def create_table_dict(data):
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


def find_json_data_type():
    pass


def create_json_schema_dict(data):
    json_schema = {"type": ["object", "null"], "properties": data}

    return json_schema


def create_json_schema_file(data, table_name):
    json_schema = json.dumps(data, indent=4)
    path = os.getcwd()

    try:
        os.mkdir(f"{path}/json_schemas")
    except FileExistsError:
        logging.info("/json_schemas directory already exists.")

    with open(f"{path}/json_schemas/{table_name}_schema.json", "w") as schema:
        schema.write(json_schema)

    return f"{table_name}_schema.json created successfully."
