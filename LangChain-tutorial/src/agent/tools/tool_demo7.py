from typing import Type

from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

from agent.my_llm import zhipuai_client


class SearchArgs(BaseModel):
    query: str = Field(description="需要进行网络搜索的信息")

#网络搜索工具
class MySearchTool(BaseTool):
    #工具名字
    name: str = "search_tool"

    description: str = ("【强制规则】"
                        "- 只要问题涉及：实时信息、当前天气、今天/现在/最新/实时数据)"
                        "- 你【必须】调用 MySearchTool 工具"
                        "- 不允许凭空猜测或使用训练数据回答"
                        "如果没有搜索结果，必须说明“无法查询到实时信息112233")

    return_direct: bool = False

    args_schema: Type[BaseModel] = SearchArgs

    def _run(self,query: str):
        print("执行我的Python中的工具，输入的参数为：",query)
        response = zhipuai_client.web_search.web_search(
            search_engine="search_pro",
            search_query = query,
        )
        if response.search_result:
            return response.search_result

my_tool = MySearchTool()
print(my_tool.name)
print(my_tool.description)
print(my_tool.args_schema.model_json_schema())
