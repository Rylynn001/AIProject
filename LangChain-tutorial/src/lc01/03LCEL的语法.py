import time

from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_core.tracers import Run


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
print(chain.invoke(2,config={'max_concurrency':3}))
print("*"*50)
print((chain1 | chain).invoke(2))
print("*"*50)
new_chain = chain1 | chain
new_chain.get_graph().print_ascii()
print("*"*50)
#6.合并输入，处理中间数据
r1 = RunnableLambda(lambda x: {'key1':x})
r2 = RunnableLambda(lambda x: x['key1'] + 10)

# chain = r1 | RunnablePassthrough() | RunnablePassthrough.assign(new_key=r2) #new_key,随意定制的，代表输出的key
chain = r1 | RunnablePassthrough() | RunnablePassthrough.assign(key2=r2) #| RunnablePassthrough().pick(['new_key'])#new_key,随意定制的，代表输出的key
print(chain.invoke(2))
print("*"*50)
r1 = RunnableLambda(test1)
r2 = RunnableLambda(lambda x: int(x) + 20)
# 在假发计算中的后备选项
chain = r1.with_fallbacks([r2])# r2是r1的后备方案，r1报错的情况下
print(chain.invoke(2))
print("*"*50)
# 根据条件，动态的构建链
r1 = RunnableLambda(test1)
r2 = RunnableLambda(lambda x: [x] * 2)
#根据r1的输出结果，判断，是否要执行r2
chain = r1 | RunnableLambda(lambda x: r2 if x>12 else RunnableLambda(lambda x: x))
print(chain.invoke(3))
#生命周期管理
def test4(n: int):
    time.sleep(n*2)
    return n*2
r1 = RunnableLambda(test4)

def on_start(run_obj: Run):
    """当r1节点启动的时候，自动调用"""
    print("r1启动的时间：",run_obj.start_time)
def on_end(run_obj: Run):
    """当r1节点结束的时候，自动调用"""
    print("r1结束的时间：",run_obj.end_time)


chain = r1.with_listeners(on_start=on_start, on_end=on_end)
print(chain.invoke(2))