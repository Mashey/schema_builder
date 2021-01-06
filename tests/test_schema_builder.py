from schema_builder import __version__
from schema_builder import *
from schema_builder.builder_ddl import *
from schema_builder.builder_table_list import *
import pytest
import pytest_cov


def test_version():
    assert __version__ == '0.2.0'


@pytest.mark.skip(reason="Test needs to be created.")
def test_find_data_type():
    pass


@pytest.mark.skip(reason="Test needs to be created.")
def test_create_table_dict():
    pass


@pytest.mark.skip(reason="Test needs to be created.")
def test_create_json_schema_dict():
    pass


@pytest.mark.skip(reason="Test needs to be created.")
def test_create_json_schema_file():
    pass


@pytest.mark.skip(reason="Test needs to be created.")
def test_schema_from_ddl():
    pass


@pytest.mark.skip(reason="Test needs to be created.")
def test_schema_from_table():
    pass


@pytest.mark.skip(reason="Test needs to be created.")
def test_build_json_schema():
    pass

