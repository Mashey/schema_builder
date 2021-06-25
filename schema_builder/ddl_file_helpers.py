import logging


def open_ddl_file(file: str):
    try:
        with open(f"{file}") as table:
            table_data = table.readlines()
            return table_data
    except FileNotFoundError as error:
        logging.warning(error)
        return "File not found."


def clean_data(data, database_name):
    step1 = remove_unnecessary_items(data)
    step2 = remove_new_lines(step1)
    table_schema = set_schema_name(step2, database_name)

    return table_schema


def remove_unnecessary_items(data):

    return data[4:-1]


def remove_new_lines(data):
    new_line_list = []

    for line in data:
        stripped_line = line.strip()

        if line == data[0]:
            new_line_list.append(stripped_line[:-2])
        elif line == data[-1]:
            new_line_list.append(stripped_line.split(" "))
        else:
            new_line_list.append(stripped_line[:-1].split(" "))

    return new_line_list


def set_schema_name(data, database_name):
    table_name = data[0].split(f"{database_name}.")[1]
    table = [table_name, data[1:]]

    return table
