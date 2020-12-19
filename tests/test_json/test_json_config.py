import pytest
from configpy import json_config


def test_json_config():
    file = 'tests/test_json/config.json'
    config = json_config.JSONConfig(file)
    assert config.name == 'Begin'
    assert config.nested.one.one_bar == 1
    assert config.nested.__config__ == 9
    assert config.list[0].el1 == 0
    assert config.list[1].el2[0] == 'some_string_param1'
    assert config.list[2] == 9

def test_config_readme():
    config = json_config.JSONConfig('tests/test_json/config_readme.json')
    assert config.str_param == "some value"
    assert config.int_param == 123
    assert config.nested_param.param1 == 1
    assert config.nested_param.param2 == 2
    assert config.list_param[0].element1 == 1
    assert config.list_param[1] == 2

def test_json_config_outer_list():
    file = 'tests/test_json/config2.json'
    config = json_config.JSONConfig(file)
    assert config[0].param1 == 0
    assert config[1].param2.nested_param1 == 'some_str'

def test_json_config_exception():
    file = 'tests/test_json/config.json'
    config = json_config.JSONConfig(file)
    with pytest.raises(AttributeError):
        config.some_incorrect_attribute

def test_json_dict_exception():
    with pytest.raises(TypeError):
        json_config.JSONConfig.config_from_dict([])

def test_json_list_exception():
    with pytest.raises(TypeError):
        json_config.JSONConfig.config_from_list({})

def test_illgal_config_value():
    file = 'tests/test_json/illegal_config.json'
    with pytest.raises(AttributeError):
        json_config.JSONConfig(file)

def test_single_config_value():
    file = 'tests/test_json/single_element.json'
    config = json_config.JSONConfig(file)
    assert config[0] == 'element'
