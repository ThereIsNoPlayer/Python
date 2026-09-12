from pydantic import BaseModel,Field
class GoodsCreate(BaseModel):
    '''新增商品的请求体'''
    name:str =Field(...,description="产品名")
    price:float=Field(...,description="价格")
    stock:int=Field(...,description="库存")

class GoodsInfo(BaseModel):
    '''商品信息响应'''
    id:int=Field(...,description="商品id")
    name:str=Field(...,description="产品名")
    price:float=Field(...,description="价格")
    stock:int=Field(...,description="库存")
    