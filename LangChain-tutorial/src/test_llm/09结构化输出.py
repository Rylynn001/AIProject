from langchain_core.output_parsers import SimpleJsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from agent.my_llm import llm

prompt = ChatPromptTemplate.from_template(
    "尽你所能回答用户问题。”"
    '你必须始终输出一个包含"answer"和"followup_question"键的JSON对象。其中"answer"代表：对用户问题的回答；"followup_question"'
    '{question}'
)

chain = prompt | llm | SimpleJsonOutputParser()
resp = chain.invoke({"question":"细胞的源动力是什么？"})
print(resp)
resp.pretty_print()