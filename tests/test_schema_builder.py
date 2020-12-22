from schema_builder import __version__
from source_ddl_builder import *
import pytest


def test_version():
    assert __version__ == '0.1.0'
