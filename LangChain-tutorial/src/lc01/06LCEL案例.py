# 需求：用户会问道各种领域的问题，根据不同的领域，定义不同的提示词模板。动态的选择合适的任务模板去完成
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RouterRunnable, RunnableSequence

from agent.my_llm import llm

#定义物理任务模板
physic_template = ChatPromptTemplate.from_template(
    "你是一个物理学教授，擅长用简洁易懂的方式回答物理问题。一下是问题的内容：{input}"
)
#定义数学任务模板
math_template = ChatPromptTemplate.from_template(
    "你是一个数学家，擅长分步骤解决数学问题，并提供详细的解决过程，以下是问题内容：{input}"
)
history_template = ChatPromptTemplate.from_template(
    "你是一个历史学家，对历史时间和背景都有深入研究，以下是问题的内容：{input}"
)
#定义计算机科学任务模板
computerscience_template = ChatPromptTemplate.from_template(
    "你是一个计算机科学家，擅长算法,数据结构和编程问题,对计算机领域都有深入研究，以下是问题的内容：{input}"
)
#默认模板
defalt_template = ChatPromptTemplate.from_template(
    "输入内容无法归类,请直接回答{input}"
)
defalt_chain = defalt_template | llm
physic_chain = physic_template | llm
math_chain = math_template | llm
history_chain = history_template | llm
computerscience_chain = computerscience_template | llm

# 动态路由的chain
def route(input):
    if '物理' in input['type']:
        print('1号')
        return {"key":'physics',
                "input": input['input']
                }
    elif '数学' in input['type']:
        print('2号')
        return {"key":'math',
                "input": input['input']
                }
    elif '历史' in input['type']:
        print('3号')
        return {"key":'history',
                "input": input['input']
                }
    elif '计算机' in input['type']:
        print('4号')
        return {"key":'computer_science',
                "input": input['input']
                }
    else:
        print('5号')
        return {"key":'defalt',
                "input": input['input']
                }
# 创建一个路由节点
route_runnable = RunnableLambda(route)

#路由调度器
router = RouterRunnable(runnables={#所有各个领域对应的任务 字典
    'physics':physic_chain,
    'math':math_chain,
    'history':history_chain,
    'computer_science':computerscience_chain,
    'defalt':defalt_chain,
})

# 第一个提示词模板:
first_prompt = ChatPromptTemplate.from_template(
    "不要回答下面用户的问题,只要根据用户的输入来判断分类,一共有[物理,历史,计算机,数学,其他]五种类别\n\n"
    "用户的输入{input}\n\n"
    "最后的输出包含分类的类别和用户输入的内容,输出格式为json,其中类别的key为type,用户输入的内容key为input"
)



chain1 = first_prompt | llm | JsonOutputParser()

chain2 = RunnableSequence(chain1,route_runnable,router,StrOutputParser()) # chain = chian1 | route_runnbble | router
inputs = [
    {"input":"什么是黑体辐射?"},
    {"input":"计算2+2的结果?"},
    {"input":"介绍一次世界大战的背景?"},
    {"input":"如何实现快速排序算法?"},
]
for inp in inputs:
    result = chain2.invoke(inp)
    print(f'问题:{inp}\n 回答:{result}')