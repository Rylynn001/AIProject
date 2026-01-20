from langchain_core.runnables import RunnableConfig
from langchain_core.tools import BaseTool, tool
from pydantic import BaseModel, Field


class SearchArgs(BaseModel):
    query: str = Field(description="需要进行网络搜索的信息")

#网络搜索工具
@tool
def get_user_info_by_name(config: RunnableConfig) -> float:
    """获取用户的所有信息，包括：性别，年龄等"""
    user_name = config['configurable'].get('user_name','zs')
    print(f"调用工具，传入的用户名是：{user_name}")
    # 模拟
    return {'username': user_name, 'sex':'男','age':18}