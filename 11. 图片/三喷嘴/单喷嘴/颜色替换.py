from PIL import Image
import numpy as np


img = Image.open('E:\\0-PhD\\1 nozzle\\本章图片\\偏差\\SW1.png')


color_list = np.unique(np.array(img).reshape(-1, len(img.getbands())), axis=0)
print(color_list)
print(len(img.getbands))