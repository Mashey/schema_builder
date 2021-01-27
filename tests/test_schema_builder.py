from schema_builder import __version__
import schema_builder as sb
import schema_builder.builder_ddl as ddl
from schema_builder.builder_table_list import *


def test_version():
    assert __version__ == '0.1.1'


def test_find_data_type_from_ddl():
    table_data = ddl.open_ddl_file('activity_table_ddl.txt')
    cleaned_ddl_data = ddl.clean_data(table_data)
    table_columns = cleaned_ddl_data[1]

    assert sb.find_data_type(table_columns[0][1]) == {'type': ['integer', 'null']}
    assert sb.find_data_type(table_columns[1][1]) == {"type": ["string", "null"]}
    assert sb.find_data_type(table_columns[3][1]) == {"type": ["string", "null"]}
    assert sb.find_data_type(table_columns[25][1]) == {"type": ["number", "null"]}


def test_find_data_type_from_formatted_table():
    table = [
        ('# col_name', 'data_type', 'comment'),
        ('activity_id', 'bigint', ''),
        ('code', 'varchar(10)', ''),
        ('description', 'varchar(60)', ''),
        ('begin_date', 'timestamp', ''),
        ('end_date', 'timestamp', ''),
        ('activity_type', 'varchar(1)', ''),
        ('block_type_dsc_id', 'bigint', ''),
        ('billable', 'varchar(1)', ''),
        ('overlap', 'varchar(1)', ''),
        ('mark_future', 'varchar(1)', ''),
        ('move_timesheet', 'varchar(1)', ''),
        ('activity_group_dsc_id', 'bigint', ''),
        ('timesheet_cat_dsc_id', 'bigint', ''),
        ('bill_unit', 'int', ''),
        ('bill_frequency', 'varchar(10)', ''),
        ('staff_unit', 'int', ''),
        ('staff_frequency', 'varchar(10)', ''),
        ('gl_code', 'varchar(10)', ''),
        ('organization_id', 'bigint', ''),
        ('created_by', 'bigint', ''),
        ('created_date', 'timestamp', ''),
        ('changed_by', 'bigint', ''),
        ('changed_date', 'timestamp', ''),
        ('unit_calculation', 'varchar(1)', ''),
        ('req_refer_phy', 'varchar(1)', ''),
        ('ndc_code_num', 'decimal(25,0)', ''),
        ('tos', 'varchar(1)', ''),
        ('nearest_unit', 'int', ''),
        ('bonus_min', 'int', ''),
        ('core_service_code_dsc_id', 'bigint', ''),
        ('modality_code_dsc_id', 'bigint', ''),
        ('crs_code', 'varchar(8)', ''),
        ('non_bill_min_yn', 'varchar(1)', ''),
        ('show_add_appt_stat_yn', 'varchar(1)', ''),
        ('darts_include_in_count', 'varchar(1)', ''),
        ('is_video_counseling', 'varchar(1)', ''),
        ('darts_activity_code', 'varchar(3)', ''),
        ('axis', 'varchar(3)', ''),
        ('cpt_type', 'varchar(1)', ''),
        ('transportation_yn', 'varchar(1)', ''),
        ('ndc_code', 'varchar(25)', ''),
        ('mobile_exportable_yn', 'varchar(1)', ''),
        ('overlap_same_activity', 'varchar(1)', ''),
        ('multiple_staff_entry_yn', 'varchar(1)', ''),
        ('activity_time_types_yn', 'varchar(1)', ''),
        ('direct_time', 'varchar(1)', ''),
        ('documentation_time', 'varchar(1)', ''),
        ('travel_time', 'varchar(1)', ''),
        ('other_time', 'varchar(1)', ''),
        ('payer_contract_yn', 'varchar(1)', ''),
        ('last_commit_time', 'timestamp', ''),
        ('last_operation', 'varchar(10)', ''),
        ('last_operation_ingest', 'timestamp', ''),
        ('last_operation_time', 'timestamp', ''),
        ('', None, None),
        ('# Detailed Table Information', None, None),
        ('Database:           ', 'brightview_prod     ', None),
        ('OwnerType:          ', 'USER                ', None),
        ('Owner:              ', 'hive                ', None),
        ('CreateTime:         ', 'Mon Nov 09 21:55:05 CST 2020', None),
        ('LastAccessTime:     ', 'UNKNOWN             ', None),
        ('Retention:          ', '0                   ', None),
        ('Location:           ',
         'hdfs://NNHA/qsi/prod/hive/brightview_prod.db/activity',
         None),
        ('Table Type:         ', 'MANAGED_TABLE       ', None),
        ('Table Parameters:', None, None),
        ('', 'COLUMN_STATS_ACCURATE', '{\\"BASIC_STATS\\":\\"true\\"}'),
        ('', 'bucketing_version   ', '2                   '),
        ('', 'numFiles            ', '6                   '),
        ('', 'numRows             ', '770                 '),
        ('', 'rawDataSize         ', '0                   '),
        ('', 'totalSize           ', '117782              '),
        ('', 'transactional       ', 'true                '),
        ('', 'transactional_properties', 'default             '),
        ('', 'transient_lastDdlTime', '1610863481          '),
        ('', None, None),
        ('# Storage Information', None, None),
        ('SerDe Library:      ', 'org.apache.hadoop.hive.ql.io.orc.OrcSerde', None),
        ('InputFormat:        ',
         'org.apache.hadoop.hive.ql.io.orc.OrcInputFormat',
         None),
        ('OutputFormat:       ',
         'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat',
         None),
        ('Compressed:         ', 'No                  ', None),
        ('Num Buckets:        ', '-1                  ', None),
        ('Bucket Columns:     ', '[]                  ', None),
        ('Sort Columns:       ', '[]                  ', None),
        ('Storage Desc Params:', None, None),
        ('', 'serialization.format', '1                   ')
    ]

    cleaned_table_data = parse_formatted_table(table, 'activity')
    table_columns = cleaned_table_data[1]

    assert sb.find_data_type(table_columns[0][1]) == {'type': ['integer', 'null']}
    assert sb.find_data_type(table_columns[1][1]) == {"type": ["string", "null"]}
    assert sb.find_data_type(table_columns[3][1]) == {"type": ["string", "null"]}
    assert sb.find_data_type(table_columns[25][1]) == {"type": ["number", "null"]}


def test_table_dict():
    table_data = ddl.open_ddl_file('activity_table_ddl.txt')
    cleaned_ddl_data = ddl.clean_data(table_data)
    table_dict = sb.create_table_dict(cleaned_ddl_data)

    assert table_dict['activity_group_dsc_id'] == {'type': ['integer', 'null']}
    assert table_dict['activity_id'] == {'type': ['integer', 'null']}
    assert table_dict['activity_time_types_yn'] == {'type': ['string', 'null']}
    assert table_dict['activity_type'] == {'type': ['string', 'null']}
    assert table_dict['axis'] == {'type': ['string', 'null']}
    assert table_dict['begin_date'] == {'type': ['string', 'null']}
    assert table_dict['bill_frequency'] == {'type': ['string', 'null']}
    assert table_dict['bill_unit'] == {'type': ['integer', 'null']}
    assert table_dict['billable'] == {'type': ['string', 'null']}
    assert table_dict['block_type_dsc_id'] == {'type': ['integer', 'null']}
    assert table_dict['bonus_min'] == {'type': ['integer', 'null']}
    assert table_dict['changed_by'] == {'type': ['integer', 'null']}
    assert table_dict['changed_date'] == {'type': ['string', 'null']}
    assert table_dict['code'] == {'type': ['string', 'null']}
    assert table_dict['core_service_code_dsc_id'] == {'type': ['integer', 'null']}
    assert table_dict['cpt_type'] == {'type': ['string', 'null']}
    assert table_dict['created_by'] == {'type': ['integer', 'null']}
    assert table_dict['created_date'] == {'type': ['string', 'null']}
    assert table_dict['crs_code'] == {'type': ['string', 'null']}
    assert table_dict['darts_activity_code'] == {'type': ['string', 'null']}
    assert table_dict['darts_include_in_count'] == {'type': ['string', 'null']}
    assert table_dict['description'] == {'type': ['string', 'null']}
    assert table_dict['direct_time'] == {'type': ['string', 'null']}
    assert table_dict['documentation_time'] == {'type': ['string', 'null']}
    assert table_dict['end_date'] == {'type': ['string', 'null']}
    assert table_dict['gl_code'] == {'type': ['string', 'null']}
    assert table_dict['is_video_counseling'] == {'type': ['string', 'null']}
    assert table_dict['last_commit_time'] == {'type': ['string', 'null']}
    assert table_dict['last_operation'] == {'type': ['string', 'null']}
    assert table_dict['last_operation_ingest'] == {'type': ['string', 'null']}
    assert table_dict['last_operation_time'] == {'type': ['string', 'null']}
    assert table_dict['mark_future'] == {'type': ['string', 'null']}
    assert table_dict['mobile_exportable_yn'] == {'type': ['string', 'null']}
    assert table_dict['modality_code_dsc_id'] == {'type': ['integer', 'null']}
    assert table_dict['move_timesheet'] == {'type': ['string', 'null']}
    assert table_dict['multiple_staff_entry_yn'] == {'type': ['string', 'null']}
    assert table_dict['ndc_code'] == {'type': ['string', 'null']}
    assert table_dict['ndc_code_num'] == {'type': ['number', 'null']}
    assert table_dict['nearest_unit'] == {'type': ['integer', 'null']}
    assert table_dict['non_bill_min_yn'] == {'type': ['string', 'null']}
    assert table_dict['organization_id'] == {'type': ['integer', 'null']}
    assert table_dict['other_time'] == {'type': ['string', 'null']}
    assert table_dict['overlap'] == {'type': ['string', 'null']}
    assert table_dict['overlap_same_activity'] == {'type': ['string', 'null']}
    assert table_dict['payer_contract_yn'] == {'type': ['string', 'null']}
    assert table_dict['req_refer_phy'] == {'type': ['string', 'null']}
    assert table_dict['show_add_appt_stat_yn'] == {'type': ['string', 'null']}
    assert table_dict['staff_frequency'] == {'type': ['string', 'null']}
    assert table_dict['staff_unit'] == {'type': ['integer', 'null']}
    assert table_dict['timesheet_cat_dsc_id'] == {'type': ['integer', 'null']}
    assert table_dict['tos'] == {'type': ['string', 'null']}
    assert table_dict['transportation_yn'] == {'type': ['string', 'null']}
    assert table_dict['travel_time'] == {'type': ['string', 'null']}
    assert table_dict['unit_calculation'] == {'type': ['string', 'null']}


def test_create_json_schema_dict():
    table_data = ddl.open_ddl_file('activity_table_ddl.txt')
    cleaned_ddl_data = ddl.clean_data(table_data)
    table_dict = sb.create_table_dict(cleaned_ddl_data)
    json_schema_dict = sb.create_json_schema_dict(table_dict)

    assert json_schema_dict['type'] == ['object', 'null']
    assert json_schema_dict['properties'] == table_dict


def test_create_json_schema_file():
    table_data = ddl.open_ddl_file('activity_table_ddl.txt')
    cleaned_ddl_data = ddl.clean_data(table_data)
    table_dict = sb.create_table_dict(cleaned_ddl_data)
    json_schema_dict = sb.create_json_schema_dict(table_dict)
    json_schema_file = sb.create_json_schema_file(json_schema_dict, 'activity')

    assert json_schema_file == 'activity_schema.json created successfully.'


def test_schema_from_ddl():
    json_schema_file = sb.schema_from_ddl('activity_table_ddl.txt')

    assert json_schema_file == 'activity_schema.json created successfully.'

    json_schema_file = sb.schema_from_ddl(None)

    assert json_schema_file == "Please enter a valid file path."


def test_schema_from_table():
    table_name = 'activity'
    table = [
        ('# col_name', 'data_type', 'comment'),
        ('activity_id', 'bigint', ''),
        ('code', 'varchar(10)', ''),
        ('description', 'varchar(60)', ''),
        ('begin_date', 'timestamp', ''),
        ('end_date', 'timestamp', ''),
        ('activity_type', 'varchar(1)', ''),
        ('block_type_dsc_id', 'bigint', ''),
        ('billable', 'varchar(1)', ''),
        ('overlap', 'varchar(1)', ''),
        ('mark_future', 'varchar(1)', ''),
        ('move_timesheet', 'varchar(1)', ''),
        ('activity_group_dsc_id', 'bigint', ''),
        ('timesheet_cat_dsc_id', 'bigint', ''),
        ('bill_unit', 'int', ''),
        ('bill_frequency', 'varchar(10)', ''),
        ('staff_unit', 'int', ''),
        ('staff_frequency', 'varchar(10)', ''),
        ('gl_code', 'varchar(10)', ''),
        ('organization_id', 'bigint', ''),
        ('created_by', 'bigint', ''),
        ('created_date', 'timestamp', ''),
        ('changed_by', 'bigint', ''),
        ('changed_date', 'timestamp', ''),
        ('unit_calculation', 'varchar(1)', ''),
        ('req_refer_phy', 'varchar(1)', ''),
        ('ndc_code_num', 'decimal(25,0)', ''),
        ('tos', 'varchar(1)', ''),
        ('nearest_unit', 'int', ''),
        ('bonus_min', 'int', ''),
        ('core_service_code_dsc_id', 'bigint', ''),
        ('modality_code_dsc_id', 'bigint', ''),
        ('crs_code', 'varchar(8)', ''),
        ('non_bill_min_yn', 'varchar(1)', ''),
        ('show_add_appt_stat_yn', 'varchar(1)', ''),
        ('darts_include_in_count', 'varchar(1)', ''),
        ('is_video_counseling', 'varchar(1)', ''),
        ('darts_activity_code', 'varchar(3)', ''),
        ('axis', 'varchar(3)', ''),
        ('cpt_type', 'varchar(1)', ''),
        ('transportation_yn', 'varchar(1)', ''),
        ('ndc_code', 'varchar(25)', ''),
        ('mobile_exportable_yn', 'varchar(1)', ''),
        ('overlap_same_activity', 'varchar(1)', ''),
        ('multiple_staff_entry_yn', 'varchar(1)', ''),
        ('activity_time_types_yn', 'varchar(1)', ''),
        ('direct_time', 'varchar(1)', ''),
        ('documentation_time', 'varchar(1)', ''),
        ('travel_time', 'varchar(1)', ''),
        ('other_time', 'varchar(1)', ''),
        ('payer_contract_yn', 'varchar(1)', ''),
        ('last_commit_time', 'timestamp', ''),
        ('last_operation', 'varchar(10)', ''),
        ('last_operation_ingest', 'timestamp', ''),
        ('last_operation_time', 'timestamp', ''),
        ('', None, None),
        ('# Detailed Table Information', None, None),
        ('Database:           ', 'brightview_prod     ', None),
        ('OwnerType:          ', 'USER                ', None),
        ('Owner:              ', 'hive                ', None),
        ('CreateTime:         ', 'Mon Nov 09 21:55:05 CST 2020', None),
        ('LastAccessTime:     ', 'UNKNOWN             ', None),
        ('Retention:          ', '0                   ', None),
        ('Location:           ',
         'hdfs://NNHA/qsi/prod/hive/brightview_prod.db/activity',
         None),
        ('Table Type:         ', 'MANAGED_TABLE       ', None),
        ('Table Parameters:', None, None),
        ('', 'COLUMN_STATS_ACCURATE', '{\\"BASIC_STATS\\":\\"true\\"}'),
        ('', 'bucketing_version   ', '2                   '),
        ('', 'numFiles            ', '6                   '),
        ('', 'numRows             ', '770                 '),
        ('', 'rawDataSize         ', '0                   '),
        ('', 'totalSize           ', '117782              '),
        ('', 'transactional       ', 'true                '),
        ('', 'transactional_properties', 'default             '),
        ('', 'transient_lastDdlTime', '1610863481          '),
        ('', None, None),
        ('# Storage Information', None, None),
        ('SerDe Library:      ', 'org.apache.hadoop.hive.ql.io.orc.OrcSerde', None),
        ('InputFormat:        ',
         'org.apache.hadoop.hive.ql.io.orc.OrcInputFormat',
         None),
        ('OutputFormat:       ',
         'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat',
         None),
        ('Compressed:         ', 'No                  ', None),
        ('Num Buckets:        ', '-1                  ', None),
        ('Bucket Columns:     ', '[]                  ', None),
        ('Sort Columns:       ', '[]                  ', None),
        ('Storage Desc Params:', None, None),
        ('', 'serialization.format', '1                   ')
    ]

    json_schema_file = sb.schema_from_table(table, table_name)

    assert json_schema_file == 'activity_schema.json created successfully.'

    json_schema_file = sb.schema_from_table(None, table_name)

    assert json_schema_file == "Please provide data from a SQL DESCRIBE FORMATTED query."

    json_schema_file = sb.schema_from_table(table, None)

    assert json_schema_file == "Please provide a table name."


def test_build_json_schema_ddl():
    json_schema_file = sb.build_json_schema('ddl', file='activity_table_ddl.txt')

    assert json_schema_file == 'activity_schema.json created successfully.'


def test_build_json_schema_table():
    table_name = 'activity'
    table = [
        ('# col_name', 'data_type', 'comment'),
        ('activity_id', 'bigint', ''),
        ('code', 'varchar(10)', ''),
        ('description', 'varchar(60)', ''),
        ('begin_date', 'timestamp', ''),
        ('end_date', 'timestamp', ''),
        ('activity_type', 'varchar(1)', ''),
        ('block_type_dsc_id', 'bigint', ''),
        ('billable', 'varchar(1)', ''),
        ('overlap', 'varchar(1)', ''),
        ('mark_future', 'varchar(1)', ''),
        ('move_timesheet', 'varchar(1)', ''),
        ('activity_group_dsc_id', 'bigint', ''),
        ('timesheet_cat_dsc_id', 'bigint', ''),
        ('bill_unit', 'int', ''),
        ('bill_frequency', 'varchar(10)', ''),
        ('staff_unit', 'int', ''),
        ('staff_frequency', 'varchar(10)', ''),
        ('gl_code', 'varchar(10)', ''),
        ('organization_id', 'bigint', ''),
        ('created_by', 'bigint', ''),
        ('created_date', 'timestamp', ''),
        ('changed_by', 'bigint', ''),
        ('changed_date', 'timestamp', ''),
        ('unit_calculation', 'varchar(1)', ''),
        ('req_refer_phy', 'varchar(1)', ''),
        ('ndc_code_num', 'decimal(25,0)', ''),
        ('tos', 'varchar(1)', ''),
        ('nearest_unit', 'int', ''),
        ('bonus_min', 'int', ''),
        ('core_service_code_dsc_id', 'bigint', ''),
        ('modality_code_dsc_id', 'bigint', ''),
        ('crs_code', 'varchar(8)', ''),
        ('non_bill_min_yn', 'varchar(1)', ''),
        ('show_add_appt_stat_yn', 'varchar(1)', ''),
        ('darts_include_in_count', 'varchar(1)', ''),
        ('is_video_counseling', 'varchar(1)', ''),
        ('darts_activity_code', 'varchar(3)', ''),
        ('axis', 'varchar(3)', ''),
        ('cpt_type', 'varchar(1)', ''),
        ('transportation_yn', 'varchar(1)', ''),
        ('ndc_code', 'varchar(25)', ''),
        ('mobile_exportable_yn', 'varchar(1)', ''),
        ('overlap_same_activity', 'varchar(1)', ''),
        ('multiple_staff_entry_yn', 'varchar(1)', ''),
        ('activity_time_types_yn', 'varchar(1)', ''),
        ('direct_time', 'varchar(1)', ''),
        ('documentation_time', 'varchar(1)', ''),
        ('travel_time', 'varchar(1)', ''),
        ('other_time', 'varchar(1)', ''),
        ('payer_contract_yn', 'varchar(1)', ''),
        ('last_commit_time', 'timestamp', ''),
        ('last_operation', 'varchar(10)', ''),
        ('last_operation_ingest', 'timestamp', ''),
        ('last_operation_time', 'timestamp', ''),
        ('', None, None),
        ('# Detailed Table Information', None, None),
        ('Database:           ', 'brightview_prod     ', None),
        ('OwnerType:          ', 'USER                ', None),
        ('Owner:              ', 'hive                ', None),
        ('CreateTime:         ', 'Mon Nov 09 21:55:05 CST 2020', None),
        ('LastAccessTime:     ', 'UNKNOWN             ', None),
        ('Retention:          ', '0                   ', None),
        ('Location:           ',
         'hdfs://NNHA/qsi/prod/hive/brightview_prod.db/activity',
         None),
        ('Table Type:         ', 'MANAGED_TABLE       ', None),
        ('Table Parameters:', None, None),
        ('', 'COLUMN_STATS_ACCURATE', '{\\"BASIC_STATS\\":\\"true\\"}'),
        ('', 'bucketing_version   ', '2                   '),
        ('', 'numFiles            ', '6                   '),
        ('', 'numRows             ', '770                 '),
        ('', 'rawDataSize         ', '0                   '),
        ('', 'totalSize           ', '117782              '),
        ('', 'transactional       ', 'true                '),
        ('', 'transactional_properties', 'default             '),
        ('', 'transient_lastDdlTime', '1610863481          '),
        ('', None, None),
        ('# Storage Information', None, None),
        ('SerDe Library:      ', 'org.apache.hadoop.hive.ql.io.orc.OrcSerde', None),
        ('InputFormat:        ',
         'org.apache.hadoop.hive.ql.io.orc.OrcInputFormat',
         None),
        ('OutputFormat:       ',
         'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat',
         None),
        ('Compressed:         ', 'No                  ', None),
        ('Num Buckets:        ', '-1                  ', None),
        ('Bucket Columns:     ', '[]                  ', None),
        ('Sort Columns:       ', '[]                  ', None),
        ('Storage Desc Params:', None, None),
        ('', 'serialization.format', '1                   ')
    ]

    json_schema_file = sb.build_json_schema('table', data=table, table_name=table_name)

    assert json_schema_file == 'activity_schema.json created successfully.'

    json_schema_file = sb.build_json_schema('blahblah', data=table, table_name=table_name)

    assert json_schema_file == "Please enter a valid source type [ddl, table]."
