import pprint
import json
from datetime import date, datetime, timezone, timedelta
from collections import defaultdict


def parse_formatted_table(table):
    end_data_index = table.index(('', None, None))
    clean_table = table[1:end_data_index]
    parsed_table = []

    for row in clean_table:
        parsed_table.append([row[0], row[1]])

    return parsed_table
