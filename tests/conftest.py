import json
import pytest


@pytest.fixture
def api_response():
    with open("tests/data/nested_json.json") as response:
        data = json.load(response)

    return data


@pytest.fixture
def ddl_data() -> list:
    table = [
        ("# col_name", "data_type", "comment"),
        ("activity_id", "bigint", ""),
        ("code", "varchar(10)", ""),
        ("description", "varchar(60)", ""),
        ("begin_date", "timestamp", ""),
        ("end_date", "timestamp", ""),
        ("activity_type", "varchar(1)", ""),
        ("block_type_dsc_id", "bigint", ""),
        ("billable", "varchar(1)", ""),
        ("overlap", "varchar(1)", ""),
        ("mark_future", "varchar(1)", ""),
        ("move_timesheet", "varchar(1)", ""),
        ("activity_group_dsc_id", "bigint", ""),
        ("timesheet_cat_dsc_id", "bigint", ""),
        ("bill_unit", "int", ""),
        ("bill_frequency", "varchar(10)", ""),
        ("staff_unit", "int", ""),
        ("staff_frequency", "varchar(10)", ""),
        ("gl_code", "varchar(10)", ""),
        ("organization_id", "bigint", ""),
        ("created_by", "bigint", ""),
        ("created_date", "timestamp", ""),
        ("changed_by", "bigint", ""),
        ("changed_date", "timestamp", ""),
        ("unit_calculation", "varchar(1)", ""),
        ("req_refer_phy", "varchar(1)", ""),
        ("ndc_code_num", "decimal(25,0)", ""),
        ("tos", "varchar(1)", ""),
        ("nearest_unit", "int", ""),
        ("bonus_min", "int", ""),
        ("core_service_code_dsc_id", "bigint", ""),
        ("modality_code_dsc_id", "bigint", ""),
        ("crs_code", "varchar(8)", ""),
        ("non_bill_min_yn", "varchar(1)", ""),
        ("show_add_appt_stat_yn", "varchar(1)", ""),
        ("darts_include_in_count", "varchar(1)", ""),
        ("is_video_counseling", "varchar(1)", ""),
        ("darts_activity_code", "varchar(3)", ""),
        ("axis", "varchar(3)", ""),
        ("cpt_type", "varchar(1)", ""),
        ("transportation_yn", "varchar(1)", ""),
        ("ndc_code", "varchar(25)", ""),
        ("mobile_exportable_yn", "varchar(1)", ""),
        ("overlap_same_activity", "varchar(1)", ""),
        ("multiple_staff_entry_yn", "varchar(1)", ""),
        ("activity_time_types_yn", "varchar(1)", ""),
        ("direct_time", "varchar(1)", ""),
        ("documentation_time", "varchar(1)", ""),
        ("travel_time", "varchar(1)", ""),
        ("other_time", "varchar(1)", ""),
        ("payer_contract_yn", "varchar(1)", ""),
        ("last_commit_time", "timestamp", ""),
        ("last_operation", "varchar(10)", ""),
        ("last_operation_ingest", "timestamp", ""),
        ("last_operation_time", "timestamp", ""),
        ("", None, None),
        ("# Detailed Table Information", None, None),
        ("Database:           ", "brightview_prod     ", None),
        ("OwnerType:          ", "USER                ", None),
        ("Owner:              ", "hive                ", None),
        ("CreateTime:         ", "Mon Nov 09 21:55:05 CST 2020", None),
        ("LastAccessTime:     ", "UNKNOWN             ", None),
        ("Retention:          ", "0                   ", None),
        (
            "Location:           ",
            "hdfs://NNHA/qsi/prod/hive/brightview_prod.db/activity",
            None,
        ),
        ("Table Type:         ", "MANAGED_TABLE       ", None),
        ("Table Parameters:", None, None),
        ("", "COLUMN_STATS_ACCURATE", '{\\"BASIC_STATS\\":\\"true\\"}'),
        ("", "bucketing_version   ", "2                   "),
        ("", "numFiles            ", "6                   "),
        ("", "numRows             ", "770                 "),
        ("", "rawDataSize         ", "0                   "),
        ("", "totalSize           ", "117782              "),
        ("", "transactional       ", "true                "),
        ("", "transactional_properties", "default             "),
        ("", "transient_lastDdlTime", "1610863481          "),
        ("", None, None),
        ("# Storage Information", None, None),
        ("SerDe Library:      ", "org.apache.hadoop.hive.ql.io.orc.OrcSerde", None),
        (
            "InputFormat:        ",
            "org.apache.hadoop.hive.ql.io.orc.OrcInputFormat",
            None,
        ),
        (
            "OutputFormat:       ",
            "org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat",
            None,
        ),
        ("Compressed:         ", "No                  ", None),
        ("Num Buckets:        ", "-1                  ", None),
        ("Bucket Columns:     ", "[]                  ", None),
        ("Sort Columns:       ", "[]                  ", None),
        ("Storage Desc Params:", None, None),
        ("", "serialization.format", "1                   "),
    ]

    return table