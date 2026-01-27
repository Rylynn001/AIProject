from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个边塞诗人，可以作诗"),
        MessagesPlaceholder("history"),
        ("system","请再来一首唐诗")
    ]
)
history_data = [
    ("human","你来作一首唐诗"),
    ("ai","床前明月光，疑是地上霜，举头望明月，低头思故乡"),
    ("好诗，再来一个"),
    ("ai","锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
]
prompt_text = chat_prompt_template.invoke({"history":history_data}).to_string()
model = ChatTongyi(model = "qwen3-max",
                   api_key="sk-2ba8138bbb26403fb03a97f554c175bc")
res = model.invoke(prompt_text)
print(res.content,"\n",
      type(res))
