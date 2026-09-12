import enum
from typing import Optional, List

from fastapi import FastAPI, Query
import uvicorn
from enum import Enum
# uvicorn apptest:app --reload --host 0.0.0.0 --port 8000
app = FastAPI(title="fastapi作业测试",description="测试用",version="1.0.0")

@app.get("/api/hello")
def hello(name):
    return {"hello":name}

@app.get("/api/user/{userid}")
def get_user(userid: int):
    '''根据用户id获取信息'''
    return {
        "code": 200,
        "data": {"userid":userid,"username":f"用户 {userid}","age":20},
    }

class UserRoles(str,Enum):
    Admin = "Admin"
    User = "User"
    Guest = "Guest"

@app.get("/api/user/role/{role}")
def get_user_role(role: UserRoles):
    '''按用户角色筛选'''
    return {"code":200,"data":{"role":role.value,"count":10}}


@app.get("/api/user/list")
def user_list(
    username: str = Query(
        ...,
        min_length=2,
        max_length=20,
        description="用户名搜索关键词"
    ),
    page: int = Query(
        1,
        ge=1,
        le=100,
        description="页码，范围1-100"
    ),
    page_size: int = Query(
        10,
        ge=1,
        le=50,
        description="每页条数，范围1-50"
    ),
    tags: Optional[List[str]] = Query(
        None,
        description="用户标签筛选"
    )
):
    return {
        "username": username,
        "page": page,
        "page_size": page_size,
        "tags": tags
    }
