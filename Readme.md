## configpy

Convert python dictionary-parsable config files into object-style attributes.

### Using with YAML config

```yaml
# config.yml
str_param: some value
int_param: 123
nested_param:
  param1: 1
  param2: 2
list_param:
  - element1: 1
  - 2
```

```python
from configpy imort yaml_config
config = yaml_config.YAMLConfig('config.yml')
assert config.str_param == "some value"
assert config.int_param == 123
assert config.nested_param.param1 == 1
assert config.nested_param.param2 == 2
assert config.list_param[0].element1 == 1
assert config.list_param[1] == 2
```

### Using with JSON config

```json
{
  "str_param": "some value",
  "int_param": 123,
  "nested_param": {
    "param1": 1,
    "param2": 2
  },
  "list_param": [
    {"element1": 1},
    2
  ]
}
```

```python
from configpy import json_config
config = json_config.JSONConfig('config.json')
assert config.str_param == "some value"
assert config.int_param == 123
assert config.nested_param.param1 == 1
assert config.nested_param.param2 == 2
assert config.list_param[0].element1 == 1
assert config.list_param[1] == 2
```
