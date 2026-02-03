from langchain_community.chat_models import ChatTongyi
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore

model = ChatTongyi(model="qwen3-max")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","以我提供的参考资料为主，简介和专业的回答用户问题，参考资料：{context}."),
        ("user","用户提问：{input}")
    ]
)
def print_prompt(prompt):
    print(prompt.to_string)
    print("*"*50)
    return prompt
vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings(model="text-embedding-v4"))

#准备一下资料
#add_texts 传入一个list【str】
vector_store.add_texts(["减肥就是要少吃多练，在减脂期间吃东西很重要，清淡少油控制卡路里摄入并运动起来","跑步是很好的运动"])
input_text = "怎么减肥？"
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# chain = retriever | prompt | model | StrOutputParser
"""
retriever:
    -输入：用户的提问 str   
    -输出：向量库的检索结果    list[Document]
prompt:
    -输入，用户的提问   dict
    -输出，完整的提示词  PromptValue
"""
def format_func(docs):
    if not docs:
        return "无相关参考资料"
    formatted_str = "["
    for doc in docs:
        formatted_str+=doc.page_content
    formatted_str+="]"
    return formatted_str

chain = ({"input": RunnablePassthrough(), "context": retriever | format_func}) | prompt | print_prompt | model | StrOutputParser()
res = chain.invoke(input_text)
print(res)

