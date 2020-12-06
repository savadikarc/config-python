'''
A module to conveniently access yaml parsed dictionary variables as class object attributes.
'''
from typing import Dict
import yaml


class AtomicConfig():

    '''
    Wrapper class for dict supporting value retrival using . operator.
    '''

    def __init__(self, attribute: Dict):
        self.attribute = attribute

    def __getattr__(self, key):
        attribute_value = self.attribute.get(key)
        if attribute_value is None:
            raise AttributeError(f'{self.attribute} has no attribute {key}')
        return attribute_value


class Config():

    '''
    Main class to access config variables.
    '''

    def __init__(self, config_file):
        self.config_file = config_file
        self.config_dict = self.load_yaml()
        self.convert_config_dict(self.config_dict)

    def __getattr__(self, key):
        try:
            return getattr(self.config, key)
        except AttributeError as error:
            raise AttributeError(error) from error

    def load_yaml(self):
        '''
        Load yaml file into python dict.
        '''
        with open(self.config_file, 'r') as handle:
            config_dict = yaml.safe_load(handle)
        return config_dict

    def convert_config_dict(self, subconfig):
        '''
        Convert outermost parsed structure.
        '''
        # Outermost
        if isinstance(subconfig, dict):
            self.config = self.config_from_dict(subconfig)
        elif isinstance(subconfig, list):
            self.config = self.config_from_list(subconfig)
        else:
            self.config = subconfig

    def config_from_dict(self, subconfig):
        '''
        Convert parsed dictionary into AtomicConfig
        '''
        if isinstance(subconfig, dict):
            # Use a dict to wrap a dict. Don't @ me.
            temp_dict = {}
            for key, value in subconfig.items():
                # Convert value to atomic config
                if isinstance(value, dict):
                    config = self.config_from_dict(value)
                elif isinstance(value, list):
                    config = self.config_from_list(value)
                else:
                    config = value # Atomic value (str, int, float, etc.)
                temp_dict[key] = config
            # Wrap
            wrapped_config = AtomicConfig(temp_dict)
        else:
            wrapped_config = subconfig
        return wrapped_config

    def config_from_list(self, subconfig_list):
        '''
        Convert list of config variables into list of AtomicConfig objects.
        '''
        if isinstance(subconfig_list, list):
            temp_list = []
            for subconfig_element in subconfig_list:
                if isinstance(subconfig_element, list):
                    config = self.config_from_list(subconfig_element)
                elif isinstance(subconfig_element, dict):
                    config = self.config_from_dict(subconfig_element)
                else:
                    config = subconfig_element
                temp_list.append(config)
        else:
            temp_list = subconfig_list
        return temp_list
