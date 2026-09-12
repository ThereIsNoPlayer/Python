import os
from langchain_openai import ChatOpenAI

API_KEY=os.environ.get("API_KEY")


chat = ChatOpenAI(
    api_key=API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen3.8-max",
    temperature=1
)

response=chat.invoke("你好，介绍一下python语言,20字以内")
print(response.content)