# -*- encoding utf-8 -*-

import cv2
import os


def cutph(dir_post):
    files = os.listdir(dir_post)
    for file in files:
        if '.PNG' in file:
            dir_post_working = dir_post + file
            os.rename(dir_post_working, dir_post_working.replace('幻灯片', ''))
            dir_post_working = dir_post_working.replace('幻灯片', '')
            print(dir_post_working)
            image_cut = cv2.imread(dir_post_working)
            image_cut = image_cut[88:2173, 605:3519]
            cv2.imwrite(dir_post_working.replace(".PNG", "-cut.png"), image_cut)
            cv2.destroyAllWindows()
        else:
            pass
    return('all done')


dir = 'E:\\0-PhD\\3 nozzle\\PICTURES_OF_CHAPTER5\\DIFFERENT_PLANES\\'
cutph(dir)