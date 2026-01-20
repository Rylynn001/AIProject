from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from agent.my_llm import llm

prompt_template = ChatPromptTemplate.from_messages([
    ("system","你是一个幽默的电视台主持人！"),
    MessagesPlaceholder("msgs")
])
prompt_template.invoke({"msg":[HumanMessage(content = "你好主持人！")]})
# print(result)
chain = prompt_template | llm
resp = chain.invoke({
    "msgs":[HumanMessage(content="你好主持人")]
})
print(resp)