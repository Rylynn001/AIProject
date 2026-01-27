from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
loader = TextLoader("./data/Python基础语法.txt", encoding="utf-8")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,  # 分段的最大字符数
    chunk_overlap=50,  # 分段之间润许重叠字符数
    # 文本自然段落分割的依据符号
    separators=["\n\n", "\n", ", ", "!", "?", ".", "!", " ", "","。","，"],
    length_function=len,
)
split_docs = splitter.split_documents(docs)
print(len(split_docs))
print(split_docs)
