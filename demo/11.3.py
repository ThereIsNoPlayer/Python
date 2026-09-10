# 4.第六章课后作业
# 必做
# 1. 准备一张带二维码图片。
# (1) 程序做裁剪预处理，转为灰度。
# (2) 调用工具识别，控制台打印识别内容。
# (3) 识别结果写入 ocr_result.txt。
# 选做
# 批量读取文件夹多张二维码，全部识别结果写入同一个 txt 文档。
from PIL import Image
import os
from pyzbar.pyzbar import decode
img=Image.open(r"C:\Users\25776\Desktop\123\Screenshot_20260910_190303_Tencent Meeting.jpg")

img_crop=img.crop((100,300,500,700))
img_crop.save('crop.jpg')

img_gray=img_crop.convert('L')
res=decode(img_gray)
with open('ocr_result.txt','w+') as f:
    for item in res:
        text=item.data.decode('utf-8')
        f.write(text+'\n')

folder=r"C:\Users\25776\Desktop\123"
for filename in os.listdir(folder):
    if filename.startswith('Screenshot_'):
        path=os.path.join(folder,filename)
        im=Image.open(path)
        res1=decode(im)
        with open('ocr_result.txt','a+') as f:
            for item in res1:
                text=item.data.decode('utf-8')
                f.write(f"{filename}\t:{text}\n")