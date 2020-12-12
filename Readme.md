## configpy

Convert python dictionary-parsable config files into object-style attributes.

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
import configpy
config = configpy.YAMLConfig('config.yml')
assert config.str_param == "some value"
assert config.int_param == 123
assert config.nested_param.param1 == 1
assert config.nested_param.param2 == 2
assert config.list_param[0].element1 = 1
assert config.list_param[1] = 2
```