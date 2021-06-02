from schema_builder.builder_ddl import *
import pytest
import pytest_cov


def test_open_ddl_file():
    table_data = open_ddl_file("activity_table_ddl.txt")

    assert "-- Drop table\n" in table_data[0]
    assert "\n" in table_data[1]
    assert "-- DROP TABLE Hive.brightview_prod.activity;\n" in table_data[2]
    assert "\n" in table_data[3]
    assert "CREATE TABLE Hive.brightview_prod.activity (\n" in table_data[4]
    assert "\tactivity_id BIGINT,\n" in table_data[5]
    assert "\tcode VARCHAR(10),\n" in table_data[6]
    assert "\tdescription VARCHAR(60),\n" in table_data[7]
    assert "\tbegin_date TIMESTAMP,\n" in table_data[8]
    assert "\tend_date TIMESTAMP,\n" in table_data[9]
    assert "\tactivity_type VARCHAR(1),\n" in table_data[10]
    assert ");\n" in table_data[-1]


def test_remove_unnecessary_items():
    table_data = open_ddl_file("activity_table_ddl.txt")

    clean_data = remove_unnecessary_items(table_data)

    assert "CREATE TABLE Hive.brightview_prod.activity (\n" in clean_data[0]
    assert "\tactivity_id BIGINT,\n" in clean_data[1]
    assert "\tcode VARCHAR(10),\n" in clean_data[2]
    assert "\tdescription VARCHAR(60),\n" in clean_data[3]
    assert "\tlast_operation_time TIMESTAMP\n" in clean_data[-1]


def test_remove_new_lines():
    table_data = open_ddl_file("activity_table_ddl.txt")
    clean_data1 = remove_unnecessary_items(table_data)
    clean_data2 = remove_new_lines(clean_data1)

    assert "CREATE TABLE Hive.brightview_prod.activity" in clean_data2[0]
    assert "activity_id" in clean_data2[1][0]
    assert "BIGINT" in clean_data2[1][1]
    assert "code" in clean_data2[2][0]
    assert "VARCHAR(10)" in clean_data2[2][1]
    assert "description" in clean_data2[3][0]
    assert "VARCHAR(60)" in clean_data2[3][1]
    assert "begin_date" in clean_data2[4][0]
    assert "TIMESTAMP" in clean_data2[5][1]


def test_set_schema_name():
    table_data = open_ddl_file("activity_table_ddl.txt")
    clean_data1 = remove_unnecessary_items(table_data)
    clean_data2 = remove_new_lines(clean_data1)

    clean_data3 = set_schema_name(clean_data2)

    assert clean_data3[0] == "activity"
    assert isinstance(clean_data3[1], list)
    assert clean_data3[1][0] == ["activity_id", "BIGINT"]
    assert clean_data3[1][1] == ["code", "VARCHAR(10)"]
    assert clean_data3[1][2] == ["description", "VARCHAR(60)"]
    assert clean_data3[1][3] == ["begin_date", "TIMESTAMP"]
    assert clean_data3[1][4] == ["end_date", "TIMESTAMP"]
    assert clean_data3[1][5] == ["activity_type", "VARCHAR(1)"]


def test_clean_data():
    table_data = open_ddl_file("activity_table_ddl.txt")
    cleaned_data = clean_data(table_data)

    assert cleaned_data[0] == "activity"
    assert isinstance(cleaned_data[1], list)
    assert cleaned_data[1][0] == ["activity_id", "BIGINT"]
    assert cleaned_data[1][1] == ["code", "VARCHAR(10)"]
    assert cleaned_data[1][2] == ["description", "VARCHAR(60)"]
    assert cleaned_data[1][3] == ["begin_date", "TIMESTAMP"]
    assert cleaned_data[1][4] == ["end_date", "TIMESTAMP"]
    assert cleaned_data[1][5] == ["activity_type", "VARCHAR(1)"]
