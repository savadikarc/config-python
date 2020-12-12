import pytest
from configpy import yaml_config


def test_yaml_yaml_config():
    file = 'tests/test_yaml/config.yml'
    config = yaml_config.YAMLConfig(file)
    assert config.name == 'Begin'
    assert config.nested.one.one_bar == 1
    assert config.nested.__config__ == 9
    assert config.list[0].el1 == 0
    assert config.list[1].el2[0] == 'some_string_param1'

def test_yaml_config_outer_list():
    file = 'tests/test_yaml/config2.yml'
    config = yaml_config.YAMLConfig(file)
    assert config[0].param1 == 0
    assert config[1].param2.nested_param1 == 'some_str'

def test_yaml_config_exception():
    file = 'tests/test_yaml/config.yml'
    config = yaml_config.YAMLConfig(file)
    with pytest.raises(AttributeError):
        config.some_incorrect_attribute

def test_yaml_dict_exception():
    with pytest.raises(TypeError):
        yaml_config.YAMLConfig.config_from_dict([])

def test_yaml_list_exception():
    with pytest.raises(TypeError):
        yaml_config.YAMLConfig.config_from_list({})

def test_config_value():
    file = 'tests/test_yaml/illegal_config.yml'
    with pytest.raises(AttributeError):
        yaml_config.YAMLConfig(file)

def test_config_value2():
    file = 'tests/test_yaml/single_element.yml'
    config = yaml_config.YAMLConfig(file)
    assert config[0] == 'element'
