"""
基于streamlit完成WEB网页上传服务
"""
import streamlit as st
from AI大模型RAG与智能体开发.p4_RAG项目案例.knowledge_base import KnowledgeBaseService
#添加网页标题
st.title("知识库更新服务")
#文件上传
uploader_file = st.file_uploader("请上传txt文件",
                            type=['txt'],
                            accept_multiple_files=False,  # False 表示仅接受一个文件的上传
                            )
if "counter" not in st.session_state:
    st.session_state["counter"] = 0
if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()
count = 0
if uploader_file is not None:
    #提取文件的信息
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size

    st.subheader(f"文件名：{file_name}")
    st.write(f"格式{file_type} | 大小：{file_size:2f} KB")

    #get_value -> bytes -> decode('utf-8')
    text = uploader_file.getvalue().decode('utf-8')
    st.write(text)
    count +=1
print(f"上传了{count}个文件")