import os, json
from typing import Sequence

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage


class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path):
        self.session_id = session_id        #会话id
        self.storage_path = storage_path    #不同会话id存储文件，所在文件夹路径
        # 完整的文件路径
        self.file_path = os.path.join(self.storage_path, self.session_id)
        #确保文件夹是存在的
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def add_message(self, messages: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)  #已有的消息列表
        all_messages.extend(messages)   #新的和已有的组成一个list

        #将数据同步写入到本地文件中
        #类对象写入文件-》 一堆二进制
        #为了方便，可以将basemessage消息转为字典（借助json模块以json字符串写入文件）
        #官方message_to_dict 单个消息对象（BasMessage类示例）-》 字典
        # new_messages = []
        # for message in messages:
        #     d = message_to_dict(message)
        #     new_messages.append(d)
        new_messages = [message_to_dict(message) for message in all_messages]
        #将数据写入文件
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(new_messages, f)
    @property   #当作成员属性用
    def messages(self) -> list[BaseMessage]:
        #当前文件内：list[字典]
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                messages_data = json.load(f)#list中都是字典
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    def clear(self) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump([], f)

