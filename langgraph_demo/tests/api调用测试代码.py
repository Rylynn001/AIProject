from langgraph_sdk import get_client
import asyncio
# 调用agent发布的API接口
client = get_client(url="http://127.0.0.1:2024") #接口地址
async def main():
    async for chunk in client.runs.stream(
        None,#是否单独创建一个线程
        "agent",#对应langgraph.json中的agent
        input={
            "messages":[{
                "role": "human",
                "content": "今天北京的天气怎么样？"
            }],
        },
        stream_mode="messages-tuple"
    ):
        # print(f"Receiving new event of type:{chunk.event}...")
        # print(chunk.data)
        if isinstance(chunk.data,list) and 'type' in chunk.data[0] and chunk.data[0]['type'] == 'AIMessageChunk':
            print(chunk.data[0]['content'], end='|')
if __name__ == '__main__':
    asyncio.run(main())