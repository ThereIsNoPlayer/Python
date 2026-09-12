import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

API_KEY = os.environ.get("API_KEY")

template = '''
    你是一个小学老师，请对{grade}年级的学生给出{topic}的作文提示。
    要求：回答不超过100字，举一个生活中的例子。
'''
prompt = PromptTemplate(
    template=template,
    input_variables=["grade", "topic"]
)

llm = ChatOpenAI(
    api_key=API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen3.8-max"
)
final_prompt = prompt.format(grade="五年级", topic="我的理想")
print(final_prompt)

response=llm.invoke(final_prompt)
print(response.content)
