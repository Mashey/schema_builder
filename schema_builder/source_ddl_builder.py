import pprint
import json
from datetime import date, datetime, timezone, timedelta
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=4, depth=3)

def open_ddl_file(file=None):
  with open('./schema_builder/source_ddl_files/activity_table_ddl.txt') as table:
    table_data = table.readlines()
    
    return table_data


def parse_table_data():
  table_data = open_ddl_file()
  table_dict = {}

  return table_dict


my_table = parse_table_data()
