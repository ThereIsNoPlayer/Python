import shutil

from fastapi import FastAPI, Form, File, HTTPException, UploadFile
import os
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.mount("/files", StaticFiles(directory=UPLOAD_FOLDER), name="files")


class UserApi(BaseModel):
    username: str = Form(...)
    email: str = Form(...)


@app.post("/api/form", summary="用户表单提交")
def submit_form(
        username: str = Form(...), email: str = Form(...)
):
    return {
        "code": 200,
        "msg": {"提交成功"},
        "data": {
            "username": username,
            "email": email,
        }
    }


@app.post("/api/upload/file", summary="文件上传")
async def upload_file(
        file: UploadFile = File(...)
):
    '''文件上传'''
    file_content = await file.read()
    return {"code": 200, "msg": {"上传成功"},
            "data": {"file_name": file.filename,
                     "size": len(file_content),
                     "content_type": file.content_type}}


@app.post("/api/upload/img", summary="图片上传")
async def upload_img(
        file: UploadFile = File(...)
):
    if not file.filename.endswith((".jpg", ".jpeg", ".png")):
        return {"code": 400, "msg": "仅能上传图片文件"}
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, 'wb') as f:
        shutil.copyfileobj(file.file, f)
    url=f"http://127.0.0.1:8000/files/{file.filename}"
    return {"code": 200,
            "msg":"上传成功",
            "data":{
                "file_name": file.filename,
                "size": os.path.getsize(file_path),
                "content_type": file.content_type,
                "url": url
            }}


