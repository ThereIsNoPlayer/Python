
from datetime import datetime

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
import os

API_KEY = os.environ.get("API_KEY")
llm = ChatOpenAI(
    api_key=API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen3.8-max",
)


@tool
def pingfang(a: float) -> float:
    '''
    :param a:输入数据
    :return: 该数据的平方值
    '''
    return a ** 2

result = pingfang.invoke({"a": 5})
print(result)

@tool
def add(a: float, b: float) -> float:
    '''
    :param a: a float
    :param b: a float
    :return: a+b
    '''
    return a + b


@tool
def sub(a: float, b: float) -> float:
    '''

    :param a: a float
    :param b: a float
    :return: a-b
    '''
    return a - b


@tool
def mul(a: float, b: float) -> float:
    '''

    :param a:
    :param b:
    :return: a*b
    '''
    return a * b

tools = [add, sub, mul]
agent = create_agent(llm, tools)

response = agent.invoke({"messages": [("user", "100 减去 45 再乘以 3，结果是多少？")]})
print(response["messages"][-1].content)



@tool
def get_current_time() -> str:
    """查询当前日期和时间"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def get_current_weekdays()->str:
    '''查询星期几'''
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return weekdays[datetime.now().weekday()]

tools=[get_current_time,get_current_weekdays]
agent=create_agent(llm,tools)
response=agent.invoke({"messages":"现在几点了?星期几了？"})
print(response["messages"][-1].content)
