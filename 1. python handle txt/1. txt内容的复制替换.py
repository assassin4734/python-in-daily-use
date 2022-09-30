# _*_ encoding utf-8 _*_

import os



# 定义目录以及处理数据的列表
file_folder = [28.5, 35.5, 40.5, 45.5, 52.5]
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
velocity = [50.35410629,45.31869566,40.28328503,35.2478744,30.21246377,25.17705314,20.14164252,15.10623189,10.07082126,5.035410629]
# 定义一级目录
for folders in file_folder:
    str_folders = str(folders)
    dir_colletion = 'F:\\PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders
    print(str_folders + ' is on processing')
# 定义二级目录
    for num in range(len(scale_factor)):
        factors = scale_factor[num]
        str_factors = str(factors)  
        dir_working = 'F:\\PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders + '\\' + str_folders + '-' + str_factors
        print(str_folders + '-' + str_factors + ' is on going')
# 定义替换变量
        scale_val = str(scale_factor[num]/10)
        velocity_val = str(velocity[num])
        new_text_v28 = "V2/" + scale_val
        new_text_v29 = "V3/" + scale_val
        new_text_v30 = "V19/" + velocity_val
        new_text_v31 = "V16/" + velocity_val
# 开始替换
        file_data = ""
        f = open(dir_working + '\\z-28.5-1-ch+.txt', "r", encoding="utf-8")
        for line in f:
            line = line.replace("V2/0.1", new_text_v28)
            line = line.replace("V3/0.1", new_text_v29)
            line = line.replace("V19/50.35", new_text_v30)
            line = line.replace("V16/50.35", new_text_v31)
            file_data += line
        f.close()
        ff = open(dir_working + '\\z-28.5-1-ch+.txt', "w", encoding="utf-8")
        ff.write(file_data)
        ff.close()
input("all done")