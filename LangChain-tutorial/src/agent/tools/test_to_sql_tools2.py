from langchain_core.tools import BaseTool


class ListTablesTool(BaseTool):
    """列出数据库中所有表以及描述"""
    name = "sql_db_list_tables"