import json
from .config import Config


class JSONConfig(Config):

    def __init__(self, config_file):

        super(JSONConfig, self).__init__(config_file)

    def parse_file(self):
        """
        Load json file into python dict.
        """
        with open(self.config_file, 'r') as handle:
            config_dict = json.loads(handle.read())
        return config_dict