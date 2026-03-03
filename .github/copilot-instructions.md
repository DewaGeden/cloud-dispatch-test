# 范式开发规则（云端 Copilot Agent 必须遵守）

## 语言规范
- 代码注释：中文
- 变量名/函数名/类名：英文
- Commit message：中文
- 文档：中文

## 项目结构
```
calculator/
├── __init__.py
├── add_sub.py       # 加法和减法
├── mul_div.py       # 乘法和除法
tests/
├── __init__.py
├── test_add_sub.py
├── test_mul_div.py
```

## 代码规范
- 每个函数必须有中文 docstring
- 使用 type hints
- 异常处理：除法必须处理除零错误
- 每个模块必须有对应的测试文件
- 测试使用 pytest

## 参考实现
请参考 `calculator/__init__.py` 中的代码风格。
