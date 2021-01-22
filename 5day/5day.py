import os
import glob
from PIL import Image
image = "./photo/*.png"
f = "./photo/new_image/"

# 获取指定目录下的所有图片

image_all  = glob.glob(image)
size = 1920,1080
m  = 0
for i in image_all:
    m = m+1
    im = Image.open(i)
    img = im.resize(size, Image.ANTIALIAS)
    file = f+("image{}".format(str(m)))
    img.save(file+".png")