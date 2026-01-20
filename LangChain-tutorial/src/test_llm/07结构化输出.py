import json
from typing import Optional

from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

from agent.my_llm import llm


#生成一个笑话的段子：三个属性

#使用pydantic定义一个类
class Joke(BaseModel):
    """笑话（搞笑段子）的结构类(数据模型类POVO)"""
    setup: str = Field(description="笑话的开头部分")
    punchline: str = Field(description="笑话的包袱、笑点")
    rating: Optional[int] = Field(description="笑话的搞笑成都，范围1到10")
prompt_template = PromptTemplate.from_template("帮我生成一个关于{topic}的笑话。")
runnable = llm.with_structured_output(Joke)
chain = prompt_template | runnable
resp = chain.invoke({"topic":"猫"})
print(resp)
print(resp.__dict__)
json_str = json.dumps(resp.__dict__)
print(json_str)
