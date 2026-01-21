from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from agent.my_llm import llm

#需求： 提示词--》 llm -- 》 文本 --》提示词2--》llm--》评分
prompt1 = PromptTemplate.from_template('给我写一篇关于{key_word}的{type},字数不超过{count}')
prompt2 = PromptTemplate.from_template('给我评价一下这篇段位,总分十分你给这篇短文打分:{text_content}')
#整个需求的第一段,
chain1 = prompt1 | llm | StrOutputParser()
chain2 = chain1 | prompt2 | StrOutputParser()