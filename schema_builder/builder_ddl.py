import pprint
import json
from datetime import date, datetime, timezone, timedelta
from collections import defaultdict


def open_ddl_file(file):
    with open(f"./schema_builder/data_sources/ddl_files/{file}") as table:
        table_data = table.readlines()

        return table_data


def clean_data(data):
    step1 = remove_unnecessary_items(data)
    step2 = remove_new_lines(step1)
    table_name, table_schema = set_schema_name(step2)

    return table_name, table_schema


def remove_unnecessary_items(data):
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

