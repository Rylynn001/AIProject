from langchain_core.prompts import ChatPromptTemplate

from agent.my_llm import llm

prompt_template = ChatPromptTemplate.from_messages([
    ("system","你是一个幽默的电视台主持人！"),
    ("user","帮我生成一个简短的，关于{topic}的报幕词")
])
print(prompt_template.invoke({"topic": "相声"}))
chain = prompt_template | llm
resp = chain.invoke("{topic:舞台剧}")
print(resp)