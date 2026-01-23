from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

model = ChatTongyi(model = "qwen3-max",
                   )

messages = [
    ("system","你是一个边塞诗人"),
    ("human","写一首唐诗"),
    ("ai","锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    ("human","按照你上一个回复的格式，再写一首唐诗"),

]

#调用stream流式执行
res = model.stream(input = messages)

#for循环迭代打印输出
for chunk in res:
    print(chunk.content, end = "" ,flush=True)