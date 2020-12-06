'''
A module to conveniently access yaml parsed dictionary variables as class object attributes.
'''
import yaml
from .wrappers import KeyedConfig, IndexedConfig

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

    def __getitem__(self, index):
        if not isinstance(self.config, IndexedConfig):
            raise TypeError(f'Config is not iterable.')
        try:
            return self.config[index]
        except IndexError as error:
            raise IndexError(error) from error
        except TypeError as error:
            raise TypeError(error) from error

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
            self.config = Config.config_from_dict(subconfig)
        elif isinstance(subconfig, list):
            self.config = Config.config_from_list(subconfig)
        else:
            self.config = subconfig

    @staticmethod
    def config_from_dict(subconfig):
        '''
        Convert parsed dictionary into KeyedConfig
        '''
        if isinstance(subconfig, dict):
            # Use a dict to wrap a dict. Don't @ me.
            temp_dict = {}
            for key, value in subconfig.items():
                # Convert value to atomic config
                if isinstance(value, dict):
                    config = Config.config_from_dict(value)
                elif isinstance(value, list):
                    config = Config.config_from_list(value)
                else:
                    config = value # Atomic value (str, int, float, etc.)
                temp_dict[key] = config
            # Wrap
            wrapped_config = KeyedConfig(temp_dict)
            return wrapped_config
        else:
            raise TypeError(f'Input with type {type(subconfig)} cannot be parsed as a dict.')

    @staticmethod
    def config_from_list(subconfig_list):
        '''
        Convert list of config variables into list of KeyedConfig objects.
        '''
        if isinstance(subconfig_list, list):
            config_list = []
            for subconfig_element in subconfig_list:
                if isinstance(subconfig_element, list):
                    config = Config.config_from_list(subconfig_element)
                elif isinstance(subconfig_element, dict):
                    config = Config.config_from_dict(subconfig_element)
                else:
                    config = subconfig_element
                config_list.append(config)
            wrapped_config_list = IndexedConfig(config_list)
            return wrapped_config_list
        else:
            raise TypeError(f'Input with type {type(subconfig_list)} cannot be parsed as a list.')

if __name__ == '__main__':
    file = 'tests/config2.yml'
    conf = Config(file)
    print(conf.__dict__)