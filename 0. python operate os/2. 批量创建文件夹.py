# -*- encoding utf-8 -*-

import os



# 定义目录变量
file_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
# 定义一级目录
for folders in file_folder:
    str_folders = str(folders)
    dir_colletion = 'F:\\PhD\\1 nozzle\\eq\\postprocessing\\' + str_folders
    print(dir_colletion + ' is on processing')
# 定义二级目录
    for num in range(len(scale_factor)):
        factors = scale_factor[num]
        str_factors = str(factors) 
        dir_working = dir_colletion + '\\40.5-' + str_factors
        print(dir_working + ' is on going')
        os.makedirs(dir_working)
