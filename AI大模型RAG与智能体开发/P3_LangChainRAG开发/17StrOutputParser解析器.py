from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

parser = StrOutputParser()
model = ChatTongyi(model = "qwen3-max")
prompt = PromptTemplate.from_template(
    "我邻居性：{lastname}，刚生了{gender}，起名，金告知我名字，无需其他内容"
)
chain = prompt | model | parser | model
res = chain.invoke({"lastname": "张", "gender": "女儿"})
print(res.content)
print(type(res))
