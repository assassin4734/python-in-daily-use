# _*_ encoding utf-8 _*_


import shutil

# 定义目录变量
distance_folder = ['48', '60', '72']
nozzles_folder = ['5nozzle', '3nozzle', '1nozzle']
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
# 定义一级目录
for nozzles in nozzles_folder:
    # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle
    dir_fluent_nozzles = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\' + nozzles
    dir_post_nozzles = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\' + nozzles
    print(dir_fluent_nozzles + ' is on processing')
    # 定义二级目录
    for distance in distance_folder:
        # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48
        dir_fluent_distance = dir_fluent_nozzles + '\\' + distance
        dir_post_distance = dir_post_nozzles + '\\' + distance
        # 定义三级目录
        for num in range(len(scale_factor)):
            factors = scale_factor[num]
            str_factors = str(factors) 
            #  E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48\\48-1
            file_copy = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48\\0.5.pdf'
            target_copy = dir_fluent_distance + '\\' + distance + '-' + str_factors + '\\0.5.pdf'
            shutil.copy(file_copy, target_copy)
            print("已复制完成任务   " + target_copy)
input("输入回车退出")