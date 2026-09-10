# 1.第三章课后作业
# 必做
# 1. 使用 OpenCV 读取一张彩色图片。
# (1) 打印 shape，写出高度、宽度、通道数。
# (2) 读取坐标 y=120,x=120 像素，打印 B、G、R 数值。
# (3) 裁剪 y:80‑250；x:80‑250 区域，保存图片。
# (4) 计算 B/G/R 三个通道平均值打印输出。
# 选做
# 把裁剪区域所有像素改成纯蓝色，保存图片。

import cv2 as cv
img = cv.imread('1.jpg')
h,w,c=img.shape
print(h,w,c)
pixel=img[120,120]
print(pixel[0], pixel[1], pixel[2])
crop=img[80:250,80:250]
cv.imwrite('2.jpg',crop)
print("B通道平均",img[:,:,0].mean())
print("G通道平均",img[:,:,1].mean())
print("R通道平均",img[:,:,2].mean())
img2=cv.imread('2.jpg')
img2[:,:,2]=0
img2[:,:,1]=0
cv.imwrite('3.jpg',img2)

