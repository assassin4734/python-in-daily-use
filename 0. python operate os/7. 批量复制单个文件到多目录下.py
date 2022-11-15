# _*_ encoding utf-8 _*_


import shutil


def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
         print('Error: %s' % e.strerror)


# 定义目录以及处理数据的列表
distance_folder = ['48', '60', '72']
nozzles_folder = ['5nozzle', '3nozzle', '1nozzle']
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
d = 0.096
quantities = ['velocity.lay', 'ch+.lay', 'flame.lay']
for nozzles in nozzles_folder:
    # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle
    dir_nozzles = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\' + nozzles
    print(dir_nozzles + ' is on processing')
    for distance in distance_folder:
        # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48
        dir_distance = dir_nozzles + '\\' + distance
        for num in range(len(scale_factor)):
            str_factors = str(scale_factor[num]) 
            #  E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48\\48-1
            dir_scale = dir_distance + '\\' + distance + '-' + str_factors
            for quantity in quantities:
                try:
                    template_position = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\' + quantity
                    print('原始文件地址' + template_position)
                    de_position = dir_scale + '\\' + quantity
                    print('目标文件地址' + de_position)
                    copyFile(template_position, de_position)
                except:
                    continue
input("all done")