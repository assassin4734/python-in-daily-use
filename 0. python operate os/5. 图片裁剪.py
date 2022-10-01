# _*_ encoding utf-8 _*_

import cv2
import re
import os


eq_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
photos = ['velocity.tiff', 'flame.tiff', 'ch+.tiff']
# 定义统计物理量的目录
for folders in eq_folder:
    # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55
    dir_colletion = 'F:\\PhD\\1 nozzle\\eq\\postprocessing\\' + folders
    print(dir_colletion + ' is on processing')
    for factors in scale_factor:
        str_factors = str(factors)
        # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55\\40.5-1
        dir_position = dir_colletion + '\\40.5-' + str_factors
        print(dir_position + ' is on going')
        files = os.listdir(dir_position)
        tiffs = []
        for file in files:
            if re.search("-cut.tiff", file, re.I):
                tiffs.append(file)
                break
        if tiffs == []:
            for phs in range(len(photos)):
                phs_str = photos[phs]
                photo_position = dir_position + '\\' + phs_str
                print(photo_position)
                image_cut = cv2.imread(photo_position)
                cv2.imshow("image", image_cut)
                size = image_cut.shape[0:3]
                print(size)
                if phs == 0:
                    image_cut = image_cut[0:390, 25:730]
                else:
                    image_cut = image_cut[0:390, 25:355]
                cv2.imwrite(photo_position.strip(".tiff") + "-cut.tiff", image_cut)
                cv2.destroyAllWindows()
        else:
            print("all photos had been exported")
input("all done")