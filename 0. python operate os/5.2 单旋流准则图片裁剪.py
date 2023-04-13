# _*_ encoding utf-8 _*_

import cv2
import os


swirl_folder = ["28.5", "35.5", "40.5", "45.5", "52.5"]
scale_factor = [1, 0.5, 0.7]
photos = ['velocity.tiff', 'velocityr.tiff', 'velocityd.tiff']
# 定义统计物理量的目录
dir = 'E:\\0-PhD\\1 nozzle\\re\\postprocessing\z-'
for folders in swirl_folder:
    # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55
    dir_colletion = dir + folders
    print(dir_colletion + ' is on processing')
    for factors in scale_factor:
        str_factors = str(factors)
        # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55\\40.5-1
        dir_position = dir_colletion + '\\' + folders + '-' + str_factors
        print(dir_position + ' is on going')
        files = os.listdir(dir_position)
        for phs in range(len(photos)):
            if factors == 1:
                phs_str = 'velocity.tiff'
            else:
                phs_str = photos[phs]
            photo_position = dir_position + '\\' + phs_str
            print(photo_position)
            image_cut = cv2.imread(photo_position)
            # image_cut = cv2.resize(image_cut, dsize=(408, 221), dst=None, fx=None, fy=None, interpolation=cv2.INTER_NEAREST)
            if phs_str == 'velocityr.tiff':
                image_cut = image_cut[0:220, 0:262]
            else:
                image_cut = image_cut[0:221, 8:271]
            cv2.imwrite(photo_position.strip(".tiff") + "-cut.tiff", image_cut)
            cv2.destroyAllWindows()
        else:
            print("all photos had been exported")
input("all done")