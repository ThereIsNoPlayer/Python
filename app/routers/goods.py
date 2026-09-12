
from typing import List

from fastapi import APIRouter,status
from schemas.goods import GoodsInfo, GoodsCreate
from services import good_services
router = APIRouter(
    prefix="/goods",
    tags=["商品管理"],
    responses={404: {"description": "Not found"}},
)
@router.post("/",
             response_model=GoodsInfo,
             status_code=status.HTTP_201_CREATED,
             summary="新增商品")
def create_goods(data: GoodsCreate,):
    return good_services.create_goods(data)

@router.get("/list",
            response_model=List[GoodsInfo],
            status_code=status.HTTP_200_OK,
            summary="商品列表"
            )
def list_goods() :
    return good_services.list_goods()