from typing import Dict, List

class KeyedConfig:
    '''
    Wrapper class for dict supporting key-value retrival using . operator.
    '''
    def __init__(self, attribute: Dict):
        self.attribute = attribute

    def __getattr__(self, key):
        attribute_value = self.attribute.get(key)
        if attribute_value is None:
            raise AttributeError(f'{self.attribute} has no attribute {key}')
        return attribute_value


class IndexedConfig:
    '''
    Wrapper class for list supporting indexed retrival.
    '''
    def __init__(self, value: List):
        self.value = value

    def __getitem__(self, index):
        return self.value[index]
