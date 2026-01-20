from langchain_core.runnables import RunnableLambda, RunnableParallel


def test1(x: int):
    return x+10

#节点：标准：Runnable
r1 = RunnableLambda(test1)#把行数封装成一个组件

# res = r1.invoke(4)
# print(res)
# #2.批量调用
# res = r1.batch([4,5])
# print(res)
#3.流式调用
def test2(prompt: str):
    for item in prompt.split(' '):
        yield item
# r1 = RunnableLambda(test2)
# res = r1.stream('This is a Dog')
# for i in res:
#     print(i)
# 4. 组合链
r1 = RunnableLambda(test1) #+10
r2 = RunnableLambda(lambda x: x*2) # *2
chain1 = r1 | r2
print(chain1.invoke(2))
print("*"*50)
#5.并行运行
chain = RunnableParallel(r1=r1, r2=r2)
#max_concurrency 最大并发数
print(chain.invoke(2,config={'max_concurrency':1}))
print("*"*50)
print((chain1 | chain).invoke(2))
