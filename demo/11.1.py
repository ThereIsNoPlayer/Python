# 必做
# 1.Pillow 读取一张图片。
# (1) 打印 size、format、mode。
# (2) 读取并打印 EXIF 元数据。
# (3) 简答：像素数据与元数据 EXIF 有什么区别？mode="L" 代表什么图像？
# 选做
# jpg 另存 png 格式，对比文件大小。
from PIL import Image
img=Image.open("./1.jpg")

print("Size:", img.size)
print("Format:", img.format)
print("Mode:", img.mode)

exif_data = img.info.get("exif")
if exif_data:
    print("EXIF Data:")
    for key, value in exif_data.items():
        print(f"  {key}: {value}")
else:
    print("No EXIF data found.")

img.save("2.png")