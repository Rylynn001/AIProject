from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model = "qwen-max",
               dashscope_api_key="sk-2ba8138bbb26403fb03a97f554c175bc")
res = model.stream(input="你是谁,能做什么?")
for chunk in res:
    print(chunk,end="",flush=True)