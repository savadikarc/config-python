"""
Wrappers for dict and list to facilitate . based and indexed retrieval of params.
"""
from typing import Dict, List

class KeyedConfig:
    '''
    Wrapper class for dict supporting key-value retrival using . operator.
    '''
    def __init__(self, attribute: Dict):
        self.attribute = attribute

    def __getattr__(self, key):
        try:
            attribute_value = self.attribute[key]
            return attribute_value
        except KeyError:
            raise AttributeError(f'{self.attribute} has no attribute {key}')


class IndexedConfig:
    '''
    Wrapper class for list supporting indexed retrival.
    '''
    def __init__(self, value: List):
        self.value = value

    def __getitem__(self, index):
        try:
            return self.value[index]
        except IndexError:
            raise IndexError(f'Index {index} out of range.')
