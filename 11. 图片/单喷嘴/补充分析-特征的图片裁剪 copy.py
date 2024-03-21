# _*_ encoding utf-8 _*_


import cv2
import os


dir = 'E:\\0-PhD\\019020210023\\add_single\\ppt2\\'
phs = os.listdir(dir)
for ph in phs:
    if '.PNG' in ph:
        newph = (ph.strip('.PNG')+'.png').replace('幻灯片', '')
        os.rename(dir+ph, dir+newph)
        image = cv2.imread(dir+newph)
        image_cut = image[0:2250, 0:6287]
        cv2.imwrite((dir+newph).replace(".png", "-cut.png"), image_cut)
    elif '.png' in ph:
        newph = ph.replace('幻灯片', '')
        os.rename(dir+ph, dir+newph)
        image = cv2.imread(dir+newph)
        image_cut = image[0:2250, 0:6287]
        cv2.imwrite((dir+newph).replace(".png", "-cut.png"), image_cut)
    else:
        pass
input("all done")