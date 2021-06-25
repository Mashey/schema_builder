from schema_builder.ddl_file_helpers import open_ddl_file, clean_data
from schema_builder.ddl_table_helpers import parse_formatted_table
from schema_builder.schema_helpers import (
    create_table_dict,
    create_json_schema_dict,
    create_json_schema_file,
)


class JsonSchemaBuilder:
    def __init__(self, database_name) -> None:
        self._database_name = database_name
        self._source_type = None
        self._file = None
        self._data = None
        self._table_name = None

    def build_json_schema(self, source_type, file=None, data=None, table_name=None):
        if source_type == "ddl":
            self._source_type = source_type
            self._file = file
            self._table_name = table_name
            return self.schema_from_ddl_file()

        if source_type == "table":
            self._source_type = source_type
            self._data = data
            self._table_name = table_name
            return self.schema_from_table()

        return "Please enter a valid source type [ddl, table]."

    def schema_from_ddl_file(self):
        if self._file is None:
            return "Please enter a valid file path."

        raw_table_data = open_ddl_file(self._file)
        clean_table_data = clean_data(raw_table_data)
        table_name = clean_table_data[0]
        table_dict = create_table_dict(clean_table_data)
        json_schema_dict = create_json_schema_dict(table_dict)

        return create_json_schema_file(json_schema_dict, table_name)

    def schema_from_table(self):
        if self._data is None:
            return "Please provide data from a SQL DESCRIBE FORMATTED query."

        if self._table_name is None:
            return "Please provide a table name."

        clean_table_data = parse_formatted_table(self._data, self._table_name)
        table_dict = create_table_dict(clean_table_data)
        json_schema_dict = create_json_schema_dict(table_dict)

        return create_json_schema_file(json_schema_dict, self._table_name)
