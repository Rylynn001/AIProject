from langchain.agents import create_agent

from agent.my_llm import zhipuai_client
from agent.tools.tool_demo1 import web_search
print("🔥🔥🔥 LOADING my_agent2.py 🔥🔥🔥")
web_agent = create_agent(
    zhipuai_client,
    tools=[web_search],
    system_prompt="你是一个智能助手，尽可能的调用工具回答用户的问题。",
    name="web_agent"
)