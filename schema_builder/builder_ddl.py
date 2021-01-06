import pprint
import json
from datetime import date, datetime, timezone, timedelta
from collections import defaultdict
from schema_builder import create_table_dict, create_json_schema_dict, create_json_schema_file, find_data_type


pp = pprint.PrettyPrinter(indent=4, depth=3)


def build_json_schema(file=None):
    raw_table_data = open_ddl_file(file)
    table_name, clean_table_data = clean_data(raw_table_data)
    table_dict = create_table_dict(clean_table_data)
    json_schema_dict = create_json_schema_dict(table_dict)
    json_schema_file = create_json_schema_file(table_name, json_schema_dict)

    return json_schema_file


def open_ddl_file(file=None):
    with open(f"./schema_builder/source_ddl_files/{file}") as table:
        table_data = table.readlines()

        return table_data


def clean_data(data):
    step1 = remove_unncessary_items(data)
    step2 = remove_new_lines(step1)
    table_name, table_schema = set_schema_name(step2)

    return table_name, table_schema


def remove_unncessary_items(data):
    clean_data = data[4:-1]

    return clean_data


def remove_new_lines(data):
    new_line_list = []

    for line in data:
        if line == data[0]:
            new_line_list.append(line[:-3])
        elif line == data[-1]:
            new_line_list.append(line[1:-1].split(' '))
        else:
            new_line_list.append(line[1:-2].split(' '))

    return new_line_list


def set_schema_name(data):
    table_name = data[0].split('brightview_prod.')

    return table_name[1], data[1:]


# def create_table_dict(data):
#     table_dict = {}

#     for row in data:
#         data_type = find_data_type(row[1])
#         table_dict[row[0]] = data_type

#     return table_dict


# def find_data_type(data):
#     # I'm thinking of using data_types in place of an if/elif chain
#     data_types = {
#         'INT': {"type": ["integer", "null"]},
#         'BIGINT': {"type": ["integer", "null"]},
#         'DECIMAL': {"type": ["number", "null"]},
#         'VARCHAR': {"type": ["string", "null"]},
#         'TIMESTAMP': {"type": ["string", "null"]}
#     }

#     if 'INT' in data:
#         return {"type": ["integer", "null"]}
#     elif 'BIGINT' in data:
#         return {"type": ["integer", "null"]}
#     elif 'DECIMAL' in data:
#         return {"type": ["number", "null"]}
#     elif 'VARCHAR' in data:
#         return {"type": ["string", "null"]}
#     elif 'TIMESTAMP' in data:
#         return {"type": ["string", "null"]}


# def create_json_schema_dict(data):
#     json_schema = {
#         "type": ["object", "null"],
#         "properties": data
#     }

#     return json_schema


# def create_json_schema_file(table_name, data):
#     json_schema = json.dumps(data, indent=4)

#     with open(f"./schema_builder/schemas/{table_name}_schema.json", "w") as schema:
#         schema.write(json_schema)

#     return f"{table_name}_schema.json successfully created."


my_table = build_json_schema("activity_table_ddl.txt")