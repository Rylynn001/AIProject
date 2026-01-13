from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field, create_model

from agent.my_llm import zhipuai_client

class SearchArgs(BaseModel):
    query: str = Field(...,description="需要进行互联网查询的查询信息")

class MyWebSearchTool(BaseTool):
    name: str = "web_search" #定义工具的名称
    description: str = "使用这个工具可以进行网络搜索"
    # #第一种写法
    # args_schema =   SearchArgs #工具的参数
    #第二种写法
    def __init__(self):
        super().__init__()
        self.args_schema = create_model("SearchInput",query=(str,Field(...,description="需要进行验证")))
    def _run(self, query: str) -> str:
        try:
            response = zhipuai_client.web_search.web_search(
                search_engine="srarch_pro",
                search_query=query
            )
            if response.search_result:
                return "\n\n".join([d.content for d in response.search_result])
            return "没有搜索到任何内容"
        except Exception as e:
            print(e)
            return f"Error:{e}"

