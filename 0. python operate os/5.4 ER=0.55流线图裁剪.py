# _*_ encoding utf-8 _*_


import cv2
import os
import re

dir = 'E:\\0-PhD\\1 nozzle\\eq\\postprocessing-transport\\eq=0.55\\stream\\'
file = os.listdir(dir)
for ph in file:
    if re.search('.png', ph, re.I):
        dir_phs = dir + ph
        image_cut = cv2.imread(dir_phs,0)
        size = image_cut.shape[0:3]
        print(size)
        image_cut = cv2.cvtColor(image_cut[144:409, 191:1117], cv2.COLOR_BAYER_BG2GRAY)
        image_cut = cv2.copyMakeBorder(image_cut, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[0,0,0])
        cv2.imwrite(dir_phs.replace(".png", "-cut.png"), image_cut)
        cv2.destroyAllWindows()
print('all done')