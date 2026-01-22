from openai import OpenAI
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-2ba8138bbb26403fb03a97f554c175bc"

)
#2.调用模型
response = client.chat.completions.create(
    model = "qwen3-max",
    messages = [
        {"role":"system", "content": "你是一个Python编程专家,并且话非常多"},
        {"role":"assistant","content": "我是一个编程专家,并且话不多,你要问什么?"},
        {"role":"user","content": "输出1-10的数字,使用python代码"}
    ],
    stream = True
)

for i in response:
# i.choices[0].delta.content,
    print(i.choices[0].delta.content,
          end = " ", #每一段之间以空格分隔
          flush = True
          )
print("*"*50)
print(response)
