from langchain_core.output_parsers import SimpleJsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from agent.my_llm import llm
prompt = ChatPromptTemplate.from_template(
    "尽你所能用中文回答用户问题"#基本指令
    "你必须始终输出一个包含”title“，”year“，”director“，”rating“键的JSON对象，其中title代表电影标题，year代表电影发行年份，director代表电影导演，rating代表评分"
    "{question}"#用户问题占位符
)
chain = prompt | llm | SimpleJsonOutputParser()
resp = chain.invoke({"question":"提供电影《盗梦空间》的详细信息"})
print(resp)