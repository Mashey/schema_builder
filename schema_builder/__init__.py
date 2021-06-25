from schema_builder.ddl_file_helpers import open_ddl_file, clean_data
from schema_builder.ddl_table_helpers import parse_formatted_table
from schema_builder.schema_helpers import (
    create_table_dict,
    create_json_schema_dict,
    create_json_schema_file,
)


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
