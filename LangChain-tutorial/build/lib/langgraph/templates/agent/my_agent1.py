from langchain.agents import create_agent

from agent.my_llm import llm

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


agent = create_agent(
    llm,
    tools=[send_email],
    system_prompt="你是一个邮件助手，请始终使用 send_email 工具",
    name="agent"
)