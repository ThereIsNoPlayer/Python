from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from routers import goods
#uvicorn main:app --reload --host 0.0.0.0 --port 8000
app = FastAPI(title="商品管理系统",version="1.0.0")
app.include_router(goods.router)

@app.middleware("http")
async def middleware(request: Request,call_next):
    import time
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(f"{request.method} {request.url.path} {response.status_code} {request.headers.get('User-Agent')}")
    return response

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"code": 400, "msg": f"参数错误: {str(exc)}"}
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"code": 500, "msg": "服务器内部错误"}
    )

@app.get("/")
def root():
    return {"message": "欢迎访问，操作查看/docs"}