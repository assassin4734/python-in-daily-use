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
        find = re.search(del_subname, names, re.I)        # 正则表达式判断当前目录下是否有txt文件
        if find:
            file_list.append(names)
    numbers_of_files = len(file_list)
    return file_list, numbers_of_files



del_subname = str(input("想要删除文件的扩展名:"))
eq_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] 
for folders in eq_folder:
    # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55
    dir_colletion = 'F:\\PhD\\1 nozzle\\eq\\postprocessing\\' + folders
    print(dir_colletion + ' is on processing')
    for factors in scale_factor:
        str_factors = str(factors)
        # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55\\40.5-1
        dir_position = dir_colletion + '\\40.5-' + str_factors
        print(dir_position + ' is on going')
        file_names = os.listdir(dir_position)
        files_del = find_files(file_names)
        print(files_del[0])
        for fil_del in files_del[0]:
            os.remove(dir_position + "\\" + fil_del)
input("all done")


