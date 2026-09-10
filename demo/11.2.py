# 第五章课后作业
# 必做
# 1.Pillow 完成
# (1) 打开图片转为 numpy 数组，打印 shape。
# (2) 读取坐标 (100,100) R、G、B 像素值。
# (3) 自定义坐标裁剪图片保存。
# (4) 亮度调整为 1.7 倍保存。
# (5) 转为灰度图保存，观察图片效果。
# 选做
# numpy 数组 R 通道 G 通道互换，保存新图片观察色彩变化。

from PIL import Image
from PIL import ImageEnhance
import numpy as np

img=Image.open('1.jpg').convert('RGB')
img_arr=np.array(img)
print(img_arr.shape)
r,g,b=img.getpixel((100,100))
print(r,g,b)
crop_img=img.crop((1000,2000,2000,3000))
crop_img.save('t2.jpg')
enhancer=ImageEnhance.Brightness(img)

img_bright=enhancer.enhance(1.7)
img_bright.save('bright.jpg')

gray_img=img.convert('L')
gray_img.save('gray.jpg')

swap_arr=img_arr.copy()
swap_arr[:,:,0],swap_arr[:,:,1]=img_arr[:,:,1],img_arr[:,:,0]
swap_arr_img=Image.fromarray(swap_arr)
swap_arr_img.save('swap.jpg')


