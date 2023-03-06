# _*_ encoding utf-8 _*_

import re
import os


def find_files(current_file):
    """
    采用正则表达式判断当前目录下是否有指定文件，并进行筛选
    :param current_file:指定目录下的文件名
    :return:包含txt文件的列表
    """
    file_list = []    # 用列表储存txt文件的路径
    for names in current_file:    # 用变量存放文件地址，即文件夹名字加文件名称
        find = re.search(subname, names, re.I) 
        if find:
            file_list.append(names)
    numbers_of_files = len(file_list)
    return file_list, numbers_of_files


def name_input():
    del_subname = str(input("想要删除文件的扩展名:"))
    if del_subname == '':
        name_input()
    return del_subname


subname = name_input()
distance_folder = ['48', '60', '72']
nozzles_folder = ['5nozzle', '3nozzle', '1nozzle']
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
for nozzles in nozzles_folder:
    # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\5nozzle
    dir_nozzles = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\' + nozzles
    print(dir_nozzles + ' is on processing')
    for distance in distance_folder:
        # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\5nozzle\\48
        dir_distance = dir_nozzles + '\\' + distance
        for num in range(len(scale_factor)):
            str_factors = str(scale_factor[num]) 
            #  E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\5nozzle\\48\\48-1
            dir_scale = dir_distance + '\\' + distance + '-' + str_factors
            print(dir_scale + ' is on going')
            file_names = os.listdir(dir_scale)
            files_del = find_files(file_names)
            print(files_del[0])
            for fil_del in files_del[0]:
                os.remove(dir_scale + "\\" + fil_del)
input("all done")


