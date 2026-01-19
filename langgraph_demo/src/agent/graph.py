import os
import dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from zhipuai import ZhipuAI

from tool_demo7 import MySearchTool

# 加载 .env
dotenv.load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",   # 或你自己的模型名
    temperature=0.7,
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY1")
)

zhipuai_client = ZhipuAI(api_key="12fc198ccaca4f1faa31b74057791078.DuVfw9F76nmeRHmv")
def get_weather(city: str) -> str:
    """
    获取天气
    """
    return f"今天天气晴朗，在{city}!"
my_tool = MySearchTool
graph = create_react_agent(
    llm,
    tools=[get_weather],
    prompt="你是一个智能助手，尽可能调用工具回答用户问题"
)
