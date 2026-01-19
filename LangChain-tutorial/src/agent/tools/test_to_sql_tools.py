from typing import Optional

from langchain_core.tools import BaseTool
from pydantic import Field, create_model

from agent.utils.db_utils import MySQLDatabaseManager
from agent.utils.log_utils import log


class ListTablesTool(BaseTool):
    """列出数据库中的所有表及其描述信息"""
    name: str = "sql_db_list_tables"
    description: str = "列出MySQL数据库中的所有表名及其描述信息。"
    # 数据库管理器实例
    db_manager: MySQLDatabaseManager
    def _run(self) -> str:
        """列出数据库中的所有表及其描述信息"""
        try:
            tables_info = self.db_manager.get_tables_with_comments()
            result = f"数据库中共有 {len(tables_info)} 个表:\n\n"
            for i, table_info in enumerate(tables_info):
                table_name = table_info['table_name']
                table_comment = table_info['table_comment']

                # 处理空描述的情况
                if not table_comment or table_comment.isspace():
                    description_display = "（暂无描述）"
                else:
                    description_display = table_comment

                result += f"{i + 1}. 表名: {table_name}\n"
                result += f"   描述: {description_display}\n\n"
            return result
        except Exception as e:
            log.exception(e)
            return f"列出表信息时出错: {str(e)}"

    async def _arun(self) -> str:
        """异步执行"""
        return self._run()


class TableSchemaTool(BaseTool):
    """列出表的模式信息"""
    name: str = "sql_db_schema"
    description: str = "获取MySQL数据库中指定表的详细模式信息，包括列定义、主键、外键等。输入应为表名列表，以获取所有表信息。参数格式: {'table_names': '表名列表'}"
    db_manager: MySQLDatabaseManager

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.db_manager = db_manager
        self.args_schema = create_model(
            "TableSchemaToolArgs",
            table_names=(Optional[str],
                         Field(..., description="逗号分隔的表名列表，例如：user,students")))

    def _run(self, table_names: Optional[str] = None) -> str:
        """返回表结构信息"""
        try:
            table_list = None
            if table_names:
                table_list = [name.strip() for name in table_names.split(',') if name.strip()]
            schema_info = self.db_manager.get_table_schema(table_list)
            return schema_info if schema_info else "未找到匹配的表"
        except Exception as e:
            log.execution(e)
            return f"获取表模式信息时出错: {str(e)}"

    async def _arun(self, table_names: Optional[str] = None) -> str:
        """异步执行"""
        return self._run(table_names)


class SQLQueryTool(BaseTool):
    """执行SQL查询"""
    name: str = "sql_db_query"
    description: str = "在MySQL数据库上执行安全的SELECT查询并返回结果。输入应为有效的SQL SELECT查询语句。参数格式: {'query': 'SQL查询语句'}"
    db_manager: MySQLDatabaseManager

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.db_manager = db_manager
        self.args_schema = create_model("SQLQueryToolArgs",
                                        query=(str, Field(..., description="有效的SQL查询语句")))

    def _run(self, query: str = None) -> str:
        """执行工具逻辑"""
        try:
            if query is None:
                return "错误：未提供查询语句"
            result = self.db_manager.execute_query(query)
            return result
        except Exception as e:
            return f"执行查询时出错: {str(e)}"

    async def _arun(self, query: str = None) -> str:
        """异步执行"""
        return self._run(query)


class SQLQueryCheckerTool(BaseTool):
    """检查SQL查询语法"""
    name: str = "sql_db_query_checken"
    description: str = "检查SQL查询语句的语法是否正确，提供验证反馈。输入应为要检查的SQL查询。参数格式: {'query': 'SQL查询语句'}"
    db_manager: MySQLDatabaseManager

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.db_manager = db_manager
        self.args_schema = create_model("SQLQueryCheckerToolArgs",
                                        query=(str, Field(..., description="需要进行检查的sql语句")))

    def _run(self, query: str = None) -> str:
        """执行工具逻辑"""
        try:
            if query is None:
                return "错误：未提供查询语句"
            result = self.db_manager.validate_query(query)
            return result
        except Exception as e:
            return f"检查查询时出错: {str(e)}"

    async def _arun(self, query: str = None) -> str:
        """异步执行"""
        return self._run(query)


if __name__ == '__main__':
    connection_string = "mysql+pymysql://root:123456@127.0.0.1:3306/test_db1?charset=utf8mb4"
    db_manager = MySQLDatabaseManager(connection_string)

    # 测试第一个工具
    tool = ListTablesTool(db_manager=db_manager)
    print(tool.invoke({}))
    # 测试第二个工具
    tool = TableSchemaTool(db_manager=db_manager)
    print(tool.invoke({'table_names': 'students,scores'}))
    # 测试第三个工具
    tool = SQLQueryTool(db_manager=db_manager)
    print(tool.invoke({'query': 'select * from students'}))
    # 测试第四个工具
    tool = SQLQueryCheckerTool(db_manager=db_manager)
    print(tool.invoke({'query': 'select * from students'}))
