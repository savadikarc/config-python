import pytest
from configpy import parser

def test_parser():
    file = 'tests/config.yml'
    config = parser.Config(file)
    assert config.name == 'Begin'

def test_parser_exception():
    file = 'tests/config.yml'
    config = parser.Config(file)
    with pytest.raises(AttributeError):
        config.some_incorrect_attribute