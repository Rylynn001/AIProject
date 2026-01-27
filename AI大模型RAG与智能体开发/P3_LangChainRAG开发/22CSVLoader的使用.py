from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./data/stu.csv",
    encoding="utf-8"
)
#批量加载,.load() -> {Document,Document,...}
documents = loader.load()
for document in documents:
    print(type(document),document)