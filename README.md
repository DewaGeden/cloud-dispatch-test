# cloud-dispatch-test

云端调度者端到端测试 - Python 计算器库。本项目提供基础的四则运算功能（加法、减法、乘法、除法），用于验证云端 Copilot Agent 的代码生成与调度能力。

---

## 安装方法

### 前置要求

- Python 3.11 及以上版本

### 安装步骤

1. 克隆仓库：

   ```bash
   git clone https://github.com/DewaGeden/cloud-dispatch-test.git
   cd cloud-dispatch-test
   ```

2. 安装项目及测试依赖：

   ```bash
   pip install -e ".[test]"
   ```

---

## 使用示例

```python
from calculator.add_sub import add, subtract
from calculator.mul_div import multiply, divide

# 加法：3 + 5 = 8
result = add(3, 5)
print(result)  # 输出：8

# 减法：10 - 4 = 6
result = subtract(10, 4)
print(result)  # 输出：6

# 乘法：6 × 7 = 42
result = multiply(6, 7)
print(result)  # 输出：42

# 除法：20 ÷ 4 = 5.0
result = divide(20, 4)
print(result)  # 输出：5.0
```

---

## 运行测试

```bash
pytest
```

---

## 项目结构

```
cloud-dispatch-test/
├── calculator/
│   ├── __init__.py      # 包初始化，版本信息
│   ├── add_sub.py       # 加法和减法
│   └── mul_div.py       # 乘法和除法
├── tests/
│   ├── __init__.py
│   ├── test_add_sub.py  # 加法和减法的测试
│   └── test_mul_div.py  # 乘法和除法的测试
├── pyproject.toml       # 项目配置文件
└── README.md            # 项目说明文档
```
