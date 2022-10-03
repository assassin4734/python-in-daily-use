# -*- encoding utf-8 -*-

import os


# 定义目录变量
distance_folder = ['48', '60', '72']
nozzles_folder = ['5nozzle', '3nozzle', '1nozzle']
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
# 定义一级目录
for folders in nozzles_folder:
    # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\5nozzle
    dir_nozzles = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\' + folders
    print(dir_nozzles + ' is on processing')
    for distance in distance_folder:
        # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\5nozzle\\48
        dir_distance = dir_nozzles + '\\' + distance
    # 定义二级目录
        for num in range(len(scale_factor)):
            str_factors = str(scale_factor[num]) 
            # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\5nozzle\\48\\48-1
            dir_scale = dir_distance + '\\' + distance + '-' + str_factors
            print(dir_scale + ' is on going')
            os.makedirs(dir_scale)
