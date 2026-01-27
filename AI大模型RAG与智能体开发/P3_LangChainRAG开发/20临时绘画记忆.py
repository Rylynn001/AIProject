from langchain_community.chat_models import ChatTongyi
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableWithMessageHistory

model = ChatTongyi(model="qwen3-max")
prompt = PromptTemplate.from_template(
    "你需要根据会话历史回应用户问题，对话历史：{chat_history},用户提问：{input}，请回答"
)
str_parser = StrOutputParser()
base_chain = prompt | model | str_parser

#创建一个新的链，对原有链增强功能，自动附加历史信息
store = {}
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


conversation_chain = RunnableWithMessageHistory(
    base_chain,  # 被增强的原有的chain
    get_history,  # 通过会话id获取InmemoryChatMessageHis类对象
    input_messages_key="input",  # 表示用户输入在模板中的占位符
    history_messages_key="chat_history"  # 表示用户输入在模板中的占位符
)

if __name__ == '__main__':
    #固定格式，为当前程序配置session_id
    session_config = {
        "configurable":{
            "session_id": "user_001"
        }
    }
    res = conversation_chain.invoke({"input": "小明有两个猫"}, session_config)
    print("第一次执行：",res)

    res = conversation_chain.invoke({"input": "小刚有一只狗"}, session_config)
    print("第二次执行：",res)

    res = conversation_chain.invoke({"input": "总共有几个宠物"}, session_config)
    print("第三次执行：",res)
