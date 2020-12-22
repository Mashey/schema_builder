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
  raw_table_data = open_ddl_file()
  clean_table_data = clean_data(raw_table_data)
  table_dict = {}

  return table_dict


def clean_data(data):
  step1 = remove_opening_and_closing(data)
  step2 = remove_new_lines(step1)

  return step2


def remove_opening_and_closing(data):
  clean_data = data[4:-1]

  return clean_data


def remove_new_lines(data):
  for line in data:
    new_line = line.split('(\n')
    new_line = line.split(',\n')
    new_line = line.split('\t')
    test = 'stop'


my_table = parse_table_data()
