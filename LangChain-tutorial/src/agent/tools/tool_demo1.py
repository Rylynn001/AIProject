from langchain_core.tools import tool
@tool('my_web_search',description='互联网搜索工具，可以搜索所有的公开信息。')
def web_search(query: str) -> str:
    """互联网搜索的工具，可以搜索所有的公开的信息。

    Returns:
        返回搜索的结果信息，该信息是一个文本字符串
    """
    pass
