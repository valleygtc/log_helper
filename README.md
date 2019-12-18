# 简介：
log帮助函数。

# 使用：
将log_helper.py文件copy-paste到自己的项目中即可。

# 用法示例：
```python
from log_helper import log

@log(my_logger)
def add(a, b):
    return a + b
```

log消息如下：
```python
>>> add(1, 2)
DEBUG:my_logger:add(args=(1, 2), kwargs={}) start
DEBUG:my_logger:function add return: 3
3
```

```python
>>> add(1, '2')
DEBUG:my_logger:add(args=(1, '2'), kwargs={}) start
DEBUG:my_logger:function add raise exception: TypeError("unsupported operand type(s) for +: 'int' and 'str'")
...
```

# 开发：
- 单元测试：`python -m unittest test`
