import pytest
from configpy import parser


def test_parser():
    file = 'tests/config.yml'
    config = parser.Config(file)
    assert config.name == 'Begin'
    assert config.list[0].el1 == 0
    assert config.list[1].el2[0] == 'some_string_param1'

def test_parser_outer_list():
    file = 'tests/config2.yml'
    config = parser.Config(file)
    assert config[0].param1 == 0
    assert config[1].param2.nested_param1 == 'some_str'

def test_parser_exception():
    file = 'tests/config.yml'
    config = parser.Config(file)
    with pytest.raises(AttributeError):
        config.some_incorrect_attribute

def test_dict_exception():
    with pytest.raises(TypeError):
        parser.Config.config_from_dict([])

def test_list_exception():
    with pytest.raises(TypeError):
        parser.Config.config_from_list({})
