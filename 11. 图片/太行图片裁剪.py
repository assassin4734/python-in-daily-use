# _*_ encoding utf-8 _*_


import cv2
import os


dir = r'E:\3-work\4-other\TAIHANG\6-simulation\results'+'\\'
phs = os.listdir(dir)
for ph in phs:
    # if '.PNG' in ph:
    #     newph = (ph.strip('.PNG')+'.png').replace('幻灯片', '')
    #     os.rename(dir+ph, dir+newph)
    #     image = cv2.imread(dir+newph)
    #     image_cut = image[0:2173, 111:3650]
    #     cv2.imwrite((dir+newph).replace(".png", "-cut.png"), image_cut)
    # else:
    #     pass
    if '3' or '4' or '5' or '8' or '9' or '10' in ph:
        image = cv2.imread(dir+ph)
        image_cut = image[0:1806, 111:3650]
        cv2.imwrite((dir+ph).replace(".png", "-cut.png"), image_cut)
    else:
        pass
    # if '1' or '2' or '6' or '7' in ph:
    #     image = cv2.imread(dir+ph)
    #     image_cut = image[0:2173, 111:3650]
    #     cv2.imwrite((dir+ph).replace(".png", "-cut.png"), image_cut)
    # else:
    #     pass
input("all done")