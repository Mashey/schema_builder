from schema_builder import __version__
from schema_builder import *
from schema_builder.builder_ddl import *
from schema_builder.builder_table_list import *
import pytest
import pytest_cov


def test_version():
  assert __version__ == '0.2.0'