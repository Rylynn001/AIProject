from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from agent.my_llm import llm

gather_preferences_prompt = ChatPromptTemplate.from_template(
    "用户输入了一些餐厅的偏好：{input1}\n"
    "将用户输入的偏好总结为清晰的需求："
)
recommend_restaurants_prompt = ChatPromptTemplate.from_template(
    "这是用户的清晰需求：\n{input3}\n"
    "请总结成2-3据话，供用户快速参考："
)
get_restaurants_prompt = ChatPromptTemplate.from_template(
    "这是推荐餐厅的理由：\n{input4}\n"
    "请推荐一下北京的餐厅并附带详细地址"
)
chain = gather_preferences_prompt | llm | recommend_restaurants_prompt | llm | get_restaurants_prompt | llm | StrOutputParser()
resp = chain.invoke({'input1': '我喜欢吃辣的'})
print(resp)