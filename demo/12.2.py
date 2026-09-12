from langchain_core.prompts import ChatPromptTemplate
import os
from langchain_openai import ChatOpenAI

API_KEY=os.environ.get("API_KEY")
chat = ChatOpenAI(
    api_key=API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen3.8-max",
)

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个{style}的翻译官，把用户输入翻译成{language}。"),
    ("user", "{text}")
])
final_prompt = chat_prompt.format(
    style="专业严谨",
    language="英语",
    text="人工智能正在改变各行各业。"
)
response = chat.invoke(final_prompt)
print(response.content)