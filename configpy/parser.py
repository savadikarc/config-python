import yaml
from typing import Dict


class AtomicConfig():

    def __init__(self, attribute: Dict):
        self.attribute = attribute

    def __getattr__(self, key):
        attribute_value = self.attribute.get(key)
        if attribute_value is None:
            raise AttributeError(f'{self.attribute} has no attribute {key}')
        return attribute_value


class Config():

    def __init__(self, config_file):
        self.config_file = config_file
        self.load_yaml()
        self.convert_config_dict(self.config_dict)

    def __getattr__(self, key):

        try:
            return getattr(self.config, key)
        except AttributeError as e:
            raise AttributeError(e)

    def load_yaml(self):

        with open(self.config_file, 'r') as f:
            config_dict = yaml.safe_load(f)
        self.config_dict = config_dict

    def convert_config_dict(self, subconfig):
        
        # Outermost
        if isinstance(subconfig, dict):
            self.config = self.config_from_dict(subconfig)
        elif isinstance(subconfig, list):
            self.config = self.config_from_list(subconfig)
        else:
            self.config = subconfig

    def config_from_dict(self, subconfig):

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

    def config_from_list(self, subconfig):

        if isinstance(subconfig, list):
            temp_list = []
            for em in subconfig:
                if isinstance(em, list):
                    config = self.config_from_list(em)
                elif isinstance(em, dict):
                    config = self.config_from_dict(em)
                else:
                    config = em
                temp_list.append(config)
        else:
            temp_list = subconfig
        return temp_list


if __name__ == '__main__':
    config = Config('config.yml')
    print(config.name)
    print(config.list2)
    print(config.list2[0].el1)
    # print(config.count, type(config.count))
    # print(config.one, config.list.one.one_bar)
    # c1 = AtomicConfig(4)
    # c2 = AtomicConfig(c1, 'c1')
    # print(c1.c1)