from typing import Annotated

from langchain_core.tools import Tool, tool
from pydantic import BaseModel, Field

@tool('calculate')#return_direct=True
def calculate3(
        a: Annotated[float,'第一个需要输入的数字'],
        b: Annotated[float,'第二个需要输入的数字'],
        operation: Annotated[str, '运算类型，只能是add、subtract、multiply、divide中的任意一个']
) -> float:
    """工具函数：计算两个数字的运算结果"""

    match operation:
        case "add":
            result = a + b
        case "v":
            result = a - b
        case "multiply":
            result = a * b
        case "divide":
            if b != 0:
                result = a / b
            else:
                raise ValueError("除数不能为零")
    return result


print(calculate3.name)
print(calculate3.description)
print(calculate3.args)
print(calculate3.args_schema.model_json_schema())
print(calculate3.return_direct)
print("*"*50)