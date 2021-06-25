from schema_builder.ddl_table_helpers import parse_formatted_table


def test_parse_formatted_table(ddl_data):
    clean_data = parse_formatted_table(ddl_data, "activity")
    table_columns = clean_data[1]

    assert isinstance(clean_data, list)
    assert clean_data[0] == "activity"
    assert table_columns[0] == ["activity_id", "bigint"]
    assert table_columns[1] == ["code", "varchar(10)"]
    assert table_columns[2] == ["description", "varchar(60)"]
    assert table_columns[3] == ["begin_date", "timestamp"]
    assert table_columns[4] == ["end_date", "timestamp"]
    assert table_columns[5] == ["activity_type", "varchar(1)"]
    assert table_columns[6] == ["block_type_dsc_id", "bigint"]
    assert table_columns[7] == ["billable", "varchar(1)"]
    assert table_columns[8] == ["overlap", "varchar(1)"]
    assert table_columns[9] == ["mark_future", "varchar(1)"]
    assert table_columns[10] == ["move_timesheet", "varchar(1)"]
