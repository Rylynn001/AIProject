from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

json_parser = JsonOutputParser()
str_parser = StrOutputParser()
model = ChatTongyi(model = "qwen3-max")
first_template = PromptTemplate.from_template(
    "我的邻居姓：{lastname}，生了个{gender}，请给我起个名字，用json封装，key是name，value是值")
second_template = PromptTemplate.from_template("姓名是{name}，你评价一下这个名字")

my_func = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})

chain = first_template | model | second_template | model | str_parser
for i in chain.stream({"lastname": "张", "gender": "女"}):
    print(i,end="",flush=True)
