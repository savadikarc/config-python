"""
A module to conveniently access file-based config variables as class object attributes.
"""
import yaml
from .wrappers import KeyedConfig, IndexedConfig

class Config():

    """
    Main class to access config variables.
    """

    def __init__(self, config_file):
        self.config_file = config_file
        self.config_dict = self.parse_file()
        self.__config__ = Config.convert_config_dict(self.config_dict)

    def __getattr__(self, key):
        try:
            if not '__config__' in self.__dict__:
                raise AttributeError('Cannot retrieve attributes before Config.__init__() call.')
            return getattr(self.__config__, key)
        except AttributeError as error:
            raise AttributeError(error) from error

    def __getitem__(self, index):
        try:
            if not '__config__' in self.__dict__:
                raise AttributeError('Cannot retrieve attributes before Config.__init__() call.')
            if not isinstance(self.__config__, IndexedConfig):
                raise TypeError('Config is not iterable.')
            return self.__config__[index]
        except IndexError as error:
            raise IndexError(error) from error
        except TypeError as error:
            raise TypeError(error) from error

    def parse_file(self):
        raise NotImplementedError

    @staticmethod
    def convert_config_dict(subconfig):
        """
        Convert outermost parsed structure.
        """
        # Outermost
        if isinstance(subconfig, dict):
            if '__config__' in subconfig.keys():
                raise AttributeError('Outermost attribute name cannot match internal variable name __config__.')
            parsed_config = Config.config_from_dict(subconfig)
        elif isinstance(subconfig, list):
            parsed_config = Config.config_from_list(subconfig)
        else:
            parsed_config = IndexedConfig([subconfig])
        return parsed_config

    @staticmethod
    def config_from_dict(subconfig):
        """
        Convert parsed dictionary into KeyedConfig
        """
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
        """
        Convert list of config variables into list of KeyedConfig objects.
        """
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
