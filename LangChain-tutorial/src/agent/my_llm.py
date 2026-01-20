import os
import dotenv
from langchain_openai import ChatOpenAI
from zhipuai import ZhipuAI

# 加载 .env
dotenv.load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",   # 或你自己的模型名
    temperature=0.7,
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY1")
)
zhipuai_client = ZhipuAI(api_key="12fc198ccaca4f1faa31b74057791078.DuVfw9F76nmeRHmv")
