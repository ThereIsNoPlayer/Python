from fastapi import FastAPI, Query
from enum import Enum

# uvicorn main:app --reload --host 0.0.0.0 --port 8000
app = FastAPI(title="Goods API", description="Goods API", version="1.0.0")


@app.get("/goods_id")
def get_goods_id(goods_id: int):
    return {"goods_id": goods_id}


@app.get("/page")
def get_page(
    page: int = Query(
        1,
        ge=1,
        le=10,
    ),
    page_size: int = Query(
        10,
        ge=1,
        le=50,

    ),
):
    return {"page": page, "page_size": page_size}


@app.get("/kw")
def keywords(keywords: str =Query(
    ...,
    max_length=50,
    min_length=2,
)):
    return {"keywords": keywords}