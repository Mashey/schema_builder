import schema_builder as sb
import schema_builder.builder_ddl as ddl
from schema_builder.builder_table_list import parse_formatted_table


def test_find_ddl_data_type_from_ddl():
    table_data = ddl.open_ddl_file("activity_table_ddl.txt")
    cleaned_ddl_data = ddl.clean_data(table_data)
    table_columns = cleaned_ddl_data[1]

    assert sb.find_ddl_data_type(table_columns[0][1]) == "int"
    assert sb.find_ddl_data_type(table_columns[1][1]) == "string"
    assert sb.find_ddl_data_type(table_columns[3][1]) == "string"
    assert sb.find_ddl_data_type(table_columns[25][1]) == "float"


def test_find_ddl_data_type_from_formatted_table(ddl_data):
    cleaned_table_data = parse_formatted_table(ddl_data, "activity")
    table_columns = cleaned_table_data[1]

    assert sb.find_ddl_data_type(table_columns[0][1]) == "int"
    assert sb.find_ddl_data_type(table_columns[1][1]) == "string"
    assert sb.find_ddl_data_type(table_columns[3][1]) == "string"
    assert sb.find_ddl_data_type(table_columns[25][1]) == "float"


def test_table_dict():
    table_data = ddl.open_ddl_file("activity_table_ddl.txt")
    cleaned_ddl_data = ddl.clean_data(table_data)
    table_dict = sb.create_table_dict(cleaned_ddl_data)

    assert table_dict["activity_group_dsc_id"] == {"type": ["integer", "null"]}
    assert table_dict["activity_id"] == {"type": ["integer", "null"]}
    assert table_dict["activity_time_types_yn"] == {"type": ["string", "null"]}
    assert table_dict["activity_type"] == {"type": ["string", "null"]}
    assert table_dict["axis"] == {"type": ["string", "null"]}
    assert table_dict["begin_date"] == {"type": ["string", "null"]}
    assert table_dict["bill_frequency"] == {"type": ["string", "null"]}
    assert table_dict["bill_unit"] == {"type": ["integer", "null"]}
    assert table_dict["billable"] == {"type": ["string", "null"]}
    assert table_dict["block_type_dsc_id"] == {"type": ["integer", "null"]}
    assert table_dict["bonus_min"] == {"type": ["integer", "null"]}
    assert table_dict["changed_by"] == {"type": ["integer", "null"]}
    assert table_dict["changed_date"] == {"type": ["string", "null"]}
    assert table_dict["code"] == {"type": ["string", "null"]}
    assert table_dict["core_service_code_dsc_id"] == {"type": ["integer", "null"]}
    assert table_dict["cpt_type"] == {"type": ["string", "null"]}
    assert table_dict["created_by"] == {"type": ["integer", "null"]}
    assert table_dict["created_date"] == {"type": ["string", "null"]}
    assert table_dict["crs_code"] == {"type": ["string", "null"]}
    assert table_dict["darts_activity_code"] == {"type": ["string", "null"]}
    assert table_dict["darts_include_in_count"] == {"type": ["string", "null"]}
    assert table_dict["description"] == {"type": ["string", "null"]}
    assert table_dict["direct_time"] == {"type": ["string", "null"]}
    assert table_dict["documentation_time"] == {"type": ["string", "null"]}
    assert table_dict["end_date"] == {"type": ["string", "null"]}
    assert table_dict["gl_code"] == {"type": ["string", "null"]}
    assert table_dict["is_video_counseling"] == {"type": ["string", "null"]}
    assert table_dict["last_commit_time"] == {"type": ["string", "null"]}
    assert table_dict["last_operation"] == {"type": ["string", "null"]}
    assert table_dict["last_operation_ingest"] == {"type": ["string", "null"]}
    assert table_dict["last_operation_time"] == {"type": ["string", "null"]}
    assert table_dict["mark_future"] == {"type": ["string", "null"]}
    assert table_dict["mobile_exportable_yn"] == {"type": ["string", "null"]}
    assert table_dict["modality_code_dsc_id"] == {"type": ["integer", "null"]}
    assert table_dict["move_timesheet"] == {"type": ["string", "null"]}
    assert table_dict["multiple_staff_entry_yn"] == {"type": ["string", "null"]}
    assert table_dict["ndc_code"] == {"type": ["string", "null"]}
    assert table_dict["ndc_code_num"] == {"type": ["number", "null"]}
    assert table_dict["nearest_unit"] == {"type": ["integer", "null"]}
    assert table_dict["non_bill_min_yn"] == {"type": ["string", "null"]}
    assert table_dict["organization_id"] == {"type": ["integer", "null"]}
    assert table_dict["other_time"] == {"type": ["string", "null"]}
    assert table_dict["overlap"] == {"type": ["string", "null"]}
    assert table_dict["overlap_same_activity"] == {"type": ["string", "null"]}
    assert table_dict["payer_contract_yn"] == {"type": ["string", "null"]}
    assert table_dict["req_refer_phy"] == {"type": ["string", "null"]}


def test_create_json_schema_dict():
    table_data = ddl.open_ddl_file("activity_table_ddl.txt")
    cleaned_ddl_data = ddl.clean_data(table_data)
    table_dict = sb.create_table_dict(cleaned_ddl_data)
    json_schema_dict = sb.create_json_schema_dict(table_dict)

    assert json_schema_dict["type"] == ["object", "null"]
    assert json_schema_dict["properties"] == table_dict


def test_create_json_schema_file():
    table_data = ddl.open_ddl_file("activity_table_ddl.txt")
    cleaned_ddl_data = ddl.clean_data(table_data)
    table_dict = sb.create_table_dict(cleaned_ddl_data)
    json_schema_dict = sb.create_json_schema_dict(table_dict)
    json_schema_file = sb.create_json_schema_file(json_schema_dict, "activity")

    assert json_schema_file == "activity_schema.json created successfully."


def test_schema_from_ddl():
    json_schema_file = sb.schema_from_ddl("activity_table_ddl.txt")

    assert json_schema_file == "activity_schema.json created successfully."

    json_schema_file = sb.schema_from_ddl(None)

    assert json_schema_file == "Please enter a valid file path."


def test_schema_from_table(ddl_data):
    table_name = "activity"

    json_schema_file = sb.schema_from_table(ddl_data, table_name)

    assert json_schema_file == "activity_schema.json created successfully."

    json_schema_file = sb.schema_from_table(None, table_name)

    assert (
        json_schema_file == "Please provide data from a SQL DESCRIBE FORMATTED query."
    )

    json_schema_file = sb.schema_from_table(ddl_data, None)

    assert json_schema_file == "Please provide a table name."


def test_build_json_schema_ddl():
    json_schema_file = sb.build_json_schema("ddl", file="activity_table_ddl.txt")

    assert json_schema_file == "activity_schema.json created successfully."


def test_build_json_schema_table(ddl_data):
    table_name = "activity"

    json_schema_file = sb.build_json_schema(
        "table", data=ddl_data, table_name=table_name
    )

    assert json_schema_file == "activity_schema.json created successfully."

    json_schema_file = sb.build_json_schema(
        "blahblah", data=ddl_data, table_name=table_name
    )

    assert json_schema_file == "Please enter a valid source type [ddl, table]."
