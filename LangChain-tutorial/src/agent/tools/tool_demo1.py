from langchain_core.tools import tool
from pydantic import BaseModel, Field


@tool('my_web_search',description='互联网搜索工具，可以搜索所有的公开信息。')
def web_search(query: str) -> str:
    """互联网搜索的工具，可以搜索所有的公开的信息。

    Args:
        query: 需要进行互联网查询的信息

    Returns:
        返回搜索的结果信息，该信息是一个文本字符串
    """
    pass

class SearchArgs(BaseModel):
    query: str = Field(...,description='需要进行互联网查询的查询信息')

@tool('my_web_search2',args_schema=SearchArgs,description='互联网搜索的工具，可以搜索所有的公开的信息。',parse_docstring=True)
def web_search2(query: str) -> str:

    pass
