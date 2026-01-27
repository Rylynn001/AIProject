from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate

json_parser = JsonOutputParser()
str_parser = StrOutputParser()
model = ChatTongyi(model = "qwen3-max")
first_template = PromptTemplate.from_template(
    "我的邻居姓：{name}，生了个{gender}，请给我起个名字，用json封装，key是name，value是值")
second_template = PromptTemplate.from_template("姓名是{name}，你评价一下这个名字")
chain = first_template | model | json_parser | second_template | model | str_parser
res = chain.stream(input={"name": "张", "gender": "女"})
for i in res:
    print(i, end = "", flush= True)
