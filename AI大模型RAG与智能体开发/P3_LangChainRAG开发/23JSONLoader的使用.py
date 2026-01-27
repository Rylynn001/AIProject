from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path="./data/stus.json",
    jq_schema=".[].name",
    text_content=False,#告知JSONLoader 抽取的不是字符串
    json_lines=True #是否为jsonLines文件,默认False
)

document = loader.load()
print(document)