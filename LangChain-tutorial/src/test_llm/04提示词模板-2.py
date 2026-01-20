#步骤1：
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

from agent.my_llm import llm

examples = [
    {"question": "Python 的列表怎么去重？", "answer": "可以使用 set() 将列表转为集合再转回列表，或者用列表推导式结合 not in 去重。"},
    {"question": "Python 中如何交换两个变量的值？", "answer": "可以直接使用 a, b = b, a 来交换两个变量的值。"},
    {"question": "什么是面向对象编程？", "answer": "面向对象编程（OOP）是一种程序设计范式，通过类和对象组织代码，强调封装、继承和多态。"}
]
base_template = prompt_template = PromptTemplate.from_template("问题：{question}\n{answer}")

#步骤二：创建FewShotPromptTemplate实例
final_template = FewShotPromptTemplate(
    examples = examples,
    example_prompt=base_template, #
    suffix = "问题：{input}",
    input_variables = ["input"],
)
chain = final_template | llm
resp = chain.invoke("最小的质数是什么？")
print(resp.content)

