import yaml
from .config import Config


class YAMLConfig(Config):

    def __init__(self, config_file):

        super(YAMLConfig, self).__init__(config_file)

    def parse_file(self):
        """
        Load yaml file into python dict.
        """
        with open(self.config_file, 'r') as handle:
            config_dict = yaml.safe_load(handle)
        return config_dict
