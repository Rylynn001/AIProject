from langchain_community.llms.tongyi import Tongyi
from openai import api_key

#qwen3-max是聊天模型，qwen-max是大语言模型
model = Tongyi(model = "qwen-max",
               api_key = "sk-2ba8138bbb26403fb03a97f554c175bc")
#调用invoke向模型提问
res = model.invoke(input="你是谁呀能做什么?")
print(res)

