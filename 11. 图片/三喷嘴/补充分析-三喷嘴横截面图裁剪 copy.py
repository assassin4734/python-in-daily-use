# -*- encoding utf-8 -*-

import cv2
import os


def cutph(dir_post):
    files = os.listdir(dir_post)
    for file in files:
        if '.PNG' in file:
            dir_post_working = dir_post + file
            try:
                os.rename(dir_post_working, dir_post_working.replace('幻灯片', ''))
            except:
                pass
            dir_post_working = dir_post_working.replace('幻灯片', '')
            print(dir_post_working)
            image_cut = cv2.imread(dir_post_working)
            image_cut = image_cut[37:2173, 605:3419]
            cv2.imwrite(dir_post_working.replace(".PNG", "-cut.png"), image_cut)
            cv2.destroyAllWindows()
        else:
            pass
    return('all done')


dir = 'E:\\0-PhD\\019020210023\\add_triple\\DIFFERENT_PLANES\\'
cutph(dir)