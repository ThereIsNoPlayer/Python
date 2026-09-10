# 作业
# 简易图像预处理工具
# 1. 读取图片；打印分辨率、颜色模式；
# 2. 图片裁剪；转为灰度图保存；
# 3. 图片转为 numpy 数组，统计 R/G/B 各通道平均亮度；
# 4.OCR 识别；
# 5. 把图片信息、亮度统计、识别结果全部写入 result.txt。
# 提交：源代码 + 输出图片 + result.txt。

# import os
from PIL import Image
import cv2
import numpy as np
from pyzbar.pyzbar import decode
#default
IMAGE_FILE=r"C:\Users\25776\Desktop\123\Screenshot_20260908_190029_Tencent Meeting.jpg"
CROP_BOX=(100,400,500,700)
OUTPUT_GRAY=f'{IMAGE_FILE}_gray.png'
OUTPUT_CROP=f'{IMAGE_FILE}_crop.png'
RESULT_FILE=f'{IMAGE_FILE}_result.txt'

img=Image.open(IMAGE_FILE)
width,height=img.size
print(f"分辨率: {width} x {height}")
print(f"颜色模式: {img.mode}")

cropped=img.crop(CROP_BOX)
cropped.save(OUTPUT_CROP)

gray=cropped.convert('L')
gray.save(OUTPUT_GRAY)
print(f"裁剪区域: {CROP_BOX}")
print(f"裁剪图已保存: {OUTPUT_CROP}")
print(f"灰度图已保存: {OUTPUT_GRAY}")

arr=np.array(img)
if arr.ndim==3 and arr.shape[2]==3:
    r_m=float(np.mean(arr[:,:,0]))
    g_m=float(np.mean(arr[:,:,1]))
    b_m=float(np.mean(arr[:,:,2]))
    print(f"各通道平均亮度: R={r_m}, G={g_m}, B={b_m}")
else:
    r_m=g_m=b_m=float(np.mean(arr))
print(f"各通道平均亮度: R={r_m}, G={g_m}, B={b_m}")

gr_cv=cv2.cvtColor(np.array(cropped), cv2.COLOR_RGB2GRAY)
result=decode(gr_cv)

ocr_text=""
if result:
    for r in result:
        ocr_text += r.data.decode('utf-8')+"\n"
    print(ocr_text)
else:
    print("未识别到内容")

with open(RESULT_FILE,'w',encoding='utf-8') as f:
    f.write(f"文件名: {IMAGE_FILE}\n")
    f.write(f"分辨率: {width} x {height}\n")
    f.write(f"颜色模式: {img.mode}\n\n")
    f.write(f"裁剪区域: {CROP_BOX}\n")
    f.write(f"裁剪图保存: {OUTPUT_CROP}\n")
    f.write(f"灰度图保存: {OUTPUT_GRAY}\n\n")
    f.write(f"R 通道: {r_m:.2f}\n")
    f.write(f"G 通道: {g_m:.2f}\n")
    f.write(f"B 通道: {b_m:.2f}\n\n")
    if ocr_text:
        f.write(f"OCR 识别结果:\n{ocr_text}")
    else:
        f.write("无内容")
print(f"内容已写入:{RESULT_FILE}")