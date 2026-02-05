import time

import streamlit as st
st.title("智能客服")
st.divider()

#在页面最下方提供用户输入栏
prompt = st.chat_input()
if prompt:
    #在页面输出用户的提问
    st.chat_message("user").write(prompt)
    with st.spinner("AI思考中"):
        time.sleep(1)
    st.chat_message("assistant").write("你也好啊")
