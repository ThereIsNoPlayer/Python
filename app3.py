#
# 第四章课后作业
# 1.	定义商品信息响应模型，包含商品ID、商品名、价格、库存。
# 2.	实现统一泛型响应封装，编写接口返回商品列表。
# 3.	验证响应模型会自动过滤多余字段。
from typing import Generic, TypeVar, Optional

from pydantic import BaseModel, Field
from fastapi import FastAPI

app = FastAPI()


class GoodsInfo(BaseModel):
    Good_id: int = Field(..., description="商品id")
    Good_name: str = Field(..., description="商品名")
    Good_price: float = Field(..., description="商品价格")
    Good_stock: int = Field(..., description="库存")


@app.get("/goods", response_model=GoodsInfo)
def get_goods():
    return GoodsInfo(
        Good_id=1,
        Good_name="商品1",
        Good_price=10.0,
        Good_stock=100
    )


T = TypeVar("T")


class BaseResponse(BaseModel, Generic[T]):
    '''统一相应封装'''
    code: int = Field(1, description="响应码")
    msg: str = Field("success", description="响应信息")
    data: Optional[T] = Field(None, description="响应数据")


@app.get("/goods/list", description="获取商品信息"
    , summary="test", response_model=BaseResponse[list[GoodsInfo]])
def get_goods_list():
    goods = [
        GoodsInfo(
            Good_id=1,
            Good_name="name1",
            Good_price=10.0,
            Good_stock=100,
            password="qwe123"
        ),
        GoodsInfo(
            Good_id=2,
            Good_name="name2",
            Good_price=21.5,
            Good_stock=200,
            password="qwe123"
        )
    ]
    return BaseResponse(code=200, msg="success", data=goods)