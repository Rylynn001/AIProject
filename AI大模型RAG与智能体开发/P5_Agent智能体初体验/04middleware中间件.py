from langchain.agents import AgentState
from langchain.agents.middleware import before_agent, after_agent, before_model, after_model, wrap_model_call
from langchain_core.messages.tool import tool_call
from langchain_core.tools import tool
from langgraph.runtime import Runtime
from langgraph_api import state


@tool(description="查询天气")
def get_weather() -> str:
    return "晴天"
"""

1.agent执行前
2.agent执行后
3.model执行前
4.model执行后
5.工具执行中
6.模型执行中
"""
@before_agent
def log_before_agent(status: AgentState, runtime: Runtime) -> None:
    # agent执行前会调用这个函数并传入state和runtime两个对象
    print(f"[before agent]agent启动，并附带{len(state['messages'])}消息")

@after_agent
def log_after_agent(status: AgentState, runtime: Runtime) -> None:
    print(f"[after agent]agent结束，并附带{len(state['messages'])}消息")

@before_model
def log_before_model(status: AgentState, runtime: Runtime) -> None:
    print(f"[before model]模型即将调用，并附带{len(state['messages'])}消息")

@after_model
def log_after_model(status: AgentState, runtime: Runtime) -> None:
    print(f"[after agent]模型调用结束，并附带{len(state['messages'])}消息")

@wrap_model_call
def model_call(request, handler) -> None:
    print( "模型调用了")
    return handler(request)

@warp_tool_call
def monitor_tool(request, handler) :
    print(f"工具执行：{request,tool_call['name']}")
    print(f"工具执行传入参数")