#ICL:
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate, MessagesPlaceholder

from agent.my_llm import llm

examples = [
    {"input":"2尿2","output":"4"},
    {"input":"2尿6","output":"12"}
]
base_prompt = ChatPromptTemplate.from_messages(
    [
        ('human','{input}'),
        ('ai','{output}'),
    ]
)
#包含示例的提示词模板
few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples = examples,
    example_prompt=base_prompt,
)
final_template = ChatPromptTemplate.from_messages([
    ("system","你是只能机器人AI助手"),
    few_shot_prompt,
    MessagesPlaceholder("msgs")
])
chain = final_template | llm
resp = chain.invoke({"msgs":[HumanMessage(content="2尿5的结果是多少？")]})
print(resp)