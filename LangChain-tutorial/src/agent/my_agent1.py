from langchain.agents import create_agent, AgentState
from langchain_core.messages import AnyMessage
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt import create_react_agent

from agent.my_llm import llm
from agent.tools.tool_demo7 import MySearchTool
from agent.tools.tool_demo8 import get_user_info_by_name

print("❌❌❌ LOADING my_agent1.py ❌❌❌")

def send_email(to: str, subject: str, body: str) -> str:
    """
    发送邮件给指定收件人。

    参数:
    - to: 收件人邮箱地址
    - subject: 邮件主题
    - body: 邮件正文内容

    返回:
    - 发送结果说明
    """
    print(f"发送邮件给 {to}")
    return "邮件发送成功"

#提示词模板的函数：由用户传入内容，组成一个动态的系统提示词
def prompt(state: AgentState, config: RunnableConfig) -> list[AnyMessage]:
    user_name = config['configurable'].get('user_name','zhangsan')
    print(user_name)
    system_message = f'你是一个智能助手，当前用户的名字是：{user_name}'
    return [{'role':'system','content':system_message}] + state['messages']
agent = create_react_agent(
    llm,
    tools=[MySearchTool(),get_user_info_by_name],
    # system_prompt="""
    # 你是一个助手。
    # 只有当问题涉及【实时 / 今天 / 最新 / 当前】信息时，才可以调用 MySearchTool。
    # 如果已经有搜索结果，请直接回答，不要再次调用工具。
    # """,
    prompt=prompt,
    # name="agent"
)