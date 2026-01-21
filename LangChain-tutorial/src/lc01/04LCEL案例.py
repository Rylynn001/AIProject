from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

from agent.my_llm import llm

#需求： 提示词--》 llm -- 》 文本 --》提示词2--》llm--》评分
prompt1 = PromptTemplate.from_template('给我写一篇关于{key_word}的{type},字数不超过{count}')
prompt2 = PromptTemplate.from_template('给我评价一下这篇段位,总分十分你给这篇短文打分:{text_content}')
#整个需求的第一段,
chain1 = prompt1 | llm | StrOutputParser()
# chain2 = {'text_content': chain1} | prompt2 | llm | StrOutputParser()
# resp = chain2.invoke({'key_word': '青春','type': '散文','count':400})
# print(resp)
#第二种
def print_chain1(input):
    print(input)
    print("*"*30)
    return {'text_content': input}
chain2 = chain1 | RunnableLambda(print_chain1) | prompt2 | llm | StrOutputParser()
resp = chain2.invoke({'key_word': '青春','type': '散文','count':400})
print(resp)
