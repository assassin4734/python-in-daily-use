# _*_ encoding utf-8 _*_


import cv2
import os


dir_o = 'E:\\0-PhD\\019020210023\\add_quintuple\\'
data_val = ['MF diversity', 'MS diversity','MP diversity']
for data in data_val:
    dir = dir_o + data + '\\diversity\\'
    phs = os.listdir(dir)
    if data != 'MS diversity':
        for ph in phs:
            if '.PNG' in ph:
                newph = (ph.strip('.PNG')+'.png').replace('幻灯片', '')
                os.rename(dir+ph, dir+newph)
                image = cv2.imread(dir+newph)
                image_cut = image[0:1621, 30:2772]
                cv2.imwrite((dir+newph).replace(".png", "-cut.png"), image_cut)
            elif '.png' in ph:
                newph = ph.replace('幻灯片', '')
                os.rename(dir+ph, dir+newph)
                image = cv2.imread(dir+newph)
                image_cut = image[0:1621, 30:2772]
                cv2.imwrite((dir+newph).replace(".png", "-cut.png"), image_cut)
            else:
                pass
    else:
        for ph in phs:
            if '.PNG' in ph:
                newph = (ph.strip('.PNG')+'.png').replace('幻灯片', '')
                os.rename(dir+ph, dir+newph)
                image = cv2.imread(dir+newph)
                image_cut = image[0:1325, 50:2772]
                cv2.imwrite((dir+newph).replace(".png", "-cut.png"), image_cut)
            elif '.png' in ph:
                newph = ph.replace('幻灯片', '')
                os.rename(dir+ph, dir+newph)
                image = cv2.imread(dir+newph)
                image_cut = image[0:1325, 50:2772]
                cv2.imwrite((dir+newph).replace(".png", "-cut.png"), image_cut)
            else:
                pass
input("all done")