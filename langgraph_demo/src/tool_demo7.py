from typing import Type

from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

from src.agent.graph import zhipuai_client


class SearchArgs(BaseModel):
    query: str = Field(description="需要进行网络搜索的信息")

#网络搜索工具
class MySearchTool(BaseTool):
    #工具名字
    name: str = "search_tool"

    description: str = "搜索互联网上的公开内容，包括实时天气等等"

    return_direct: bool = False

    args_schema: Type[BaseModel] = SearchArgs

    def _run(self,query):
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
