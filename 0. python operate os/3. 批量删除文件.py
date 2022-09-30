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
file_folder = [28.5, 35.5, 40.5, 45.5, 52.5]
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] 
for folders in file_folder:
  for factors in scale_factor:
    str_folders = str(folders)
    str_factors = str(factors)
    dir_import = 'F:\\PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders + '\\' + str_folders + '-' + str_factors
    print(str_folders + "-" + str_factors + ' is on going')
    file_names = os.listdir(dir_import)
    files_del = find_files(file_names)
    print(files_del[0])
    for fil_del in files_del[0]:
        os.remove(dir_import + "\\" + fil_del)
input("all done")


