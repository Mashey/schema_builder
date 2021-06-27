from schema_builder.ddl_file_helpers import open_ddl_file, clean_data
from schema_builder.ddl_table_helpers import parse_formatted_table
from schema_builder.schema_helpers import (
    create_table_dict,
    create_json_schema_dict,
    create_json_schema_file,
)


def build_json_schema(
    source_type, file_name=None, data=None, database_name=None, table_name=None
):
    if source_type == "ddl":
        return schema_from_ddl_file(file_name, database_name)
    if source_type == "table":
        return schema_from_table(data, table_name)
    return "Please enter a valid source type [ddl, table]."


def schema_from_ddl_file(file_name: str, database_name: str):
    if not isinstance(file_name, str):
        return "Please enter a valid file path."

    if not isinstance(database_name, str):
        return "Please enter a valid database name."

    raw_table_data = open_ddl_file(file_name)
    clean_table_data = clean_data(raw_table_data, database_name)
    table_name = clean_table_data[0]
    table_dict = create_table_dict(clean_table_data)
    json_schema_dict = create_json_schema_dict(table_dict)

    return create_json_schema_file(json_schema_dict, table_name)


def schema_from_table(data: list, table_name: str):
    if not isinstance(data, list):
        return "Please provide data from a SQL DESCRIBE FORMATTED query."

    if not isinstance(table_name, str):
        return "Please provide a table name."

    clean_table_data = parse_formatted_table(data, table_name)
    table_dict = create_table_dict(clean_table_data)
    json_schema_dict = create_json_schema_dict(table_dict)

    return create_json_schema_file(json_schema_dict, table_name)


def schema_from_api():
    pass
