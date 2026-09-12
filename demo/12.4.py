# 4.任务：智能学生信息助手
# 1.	功能要求：
# ￮	成绩计算：计算学生成绩的总分、平均分（自定义工具实现）
# ￮	信息生成：生成结构化的学生信息（JSON 格式输出）
# 2.	技术要求：
# ￮	使用 PromptTemplate 管理所有提示词
# ￮	使用 OutputParser 实现结构化输出
# ￮	使用 LCEL 语法拼接基础业务链
# ￮	接入自定义计算工具，使用智能体自主调度工具
# 3.	测试场景：
# ￮	计算语文 85、数学 92、英语 78 的总分和平均分
# ￮	生成一名学生的结构化信息（姓名、年龄、专业、总分）
from urllib import response

from langchain_core.tools import tool
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
import os
from langchain.agents import create_agent
API_KEY = os.environ.get("API_KEY")
llm = ChatOpenAI(
    api_key=API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen3.8-max",
)


@tool
def calc_total(scores: list) -> float:
    """计算成绩总分，输入一个数字列表"""
    return sum(scores)


@tool
def calc_average(scores: list) -> float:
    """计算成绩平均分，输入一个数字列表"""
    return sum(scores) / len(scores)


tools = [calc_total, calc_average]


class StudentOutputInfo(BaseModel):
    name: str = Field(description='学生姓名')
    age: int = Field(description='学生年龄')
    major: str = Field(description='学生专业')
    total_score: float = Field(description='学生总分')


parser = JsonOutputParser(pydantic_object=StudentOutputInfo)

score_prompt = PromptTemplate(
    template=
    '''
    你是一个成绩计算助手
    请根据以下成绩计算总分和平均分：
    语文：{chinese}
    数学：{math}
    英语：{english}
    要求：总分和平均分都保留两位小数。
    ''',
    input_variables=['chinese', 'math', 'english']
)

info_prompt = PromptTemplate(
    template=
    '''
    请根据以下信息生成一名学生的结构化信息
    姓名：{name}
    年龄：{age}
    专业：{major}
    总分：{total}
    {format_instructions}
    '''
).partial(format_instructions=parser.get_format_instructions())

score_chain = score_prompt | llm | StrOutputParser
info_chain = info_prompt | llm | parser

scores = [85,92,78]
total_score = calc_total.invoke({"scores": scores})
average_score = calc_average.invoke({"scores": scores})
print(f"总分: {total_score}, 平均分: {average_score}")


student_data=info_chain.invoke({
    "name": "张三",
    "age": 20,
    "major": "计算机科学与技术",
    "total": total_score
})
print("结构化输出:", student_data)

agent=create_agent(llm, tools)
response =agent.invoke({
      "messages": [("user", "语文85分、数学92分、英语78分，帮我算总分和平均分")]
})
print("最终答案:", response['messages'][-1].content)
