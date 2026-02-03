from langchain.agents import create_agent
from langchain_community.chat_models import ChatTongyi

agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[],
    system_prompt="你是一个智能助手，可以回答股票相关问题，记住请告知我思考过程，让我知道你为什么调用某个工具"
)