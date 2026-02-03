from langchain_community.chat_models import ChatTongyi
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore

model = ChatTongyi(model="qwen3-max")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","以我提供的参考资料为主，简介和专业的回答用户问题，参考资料：{context}."),
        ("user","用户提问：{input}")
    ]
)

vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings(model="text-embedding-v4"))

#准备一下资料
#add_texts 传入一个list【str】
vector_store.add_texts(["减肥就是要少吃多练，在减脂期间吃东西很重要，清淡少油控制卡路里摄入并运动起来","跑步是很好的运动"])
input_text = "怎么减肥？"
result = vector_store.similarity_search(input_text, 2)
# print(type(result))
reference_text = "["
for i in result:
    reference_text+=i.page_content
reference_text+="]"
# print(reference_text)
def print_prompt(prompt):
    print(prompt.to_string)
    print("*"*50)
    return prompt
chain = prompt | print_prompt | model | StrOutputParser()
res = chain.invoke({"input": input_text, "context": reference_text})
print(res)