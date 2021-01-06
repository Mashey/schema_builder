from schema_builder import __version__
from schema_builder import build_json_schema
import pytest


def test_version():
    assert __version__ == '0.1.0'
