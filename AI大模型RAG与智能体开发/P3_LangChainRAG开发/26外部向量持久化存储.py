from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.vectorstores import InMemoryVectorStore

#Chroma 向量数据库（轻量级的）
#langchain-chroma chromadb 这里昂个库安装
vector_store = Chroma(
    collection_name="test",#当前向量存储起个名字，类似数据库表明
    embedding_function=DashScopeEmbeddings(),   #嵌入模型
    persist_directory="./chroma_db" #指定数据存放的文件夹
)
loader = CSVLoader(
    file_path="./data/info.csv",
    encoding = "utf-8",
    source_column="source", #指定本条数据的来源在哪里

)
documents = loader.load()
print(documents[0])

#向量存储的新增，删除，检索
vector_store.add_documents(
    documents=documents,    #被添加的文件，类型list【document】
    ids = ["id"+str(i) for i in range(1,len(documents)+1)]  #给添加的文档提供id（字符串）
)
#删除
vector_store.delete(["id1","id2"])
#检索
result = vector_store.similarity_search(
    "Python是不是简单易学呀",
    3,  # 检索的结果要几个
    filter={"source":"元素韩剧"}
)
print(result)
