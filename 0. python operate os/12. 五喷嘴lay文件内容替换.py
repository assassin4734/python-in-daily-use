import re, os


def find_txt(current_file):
    """
    采用正则表达式判断当前目录下是否有txt文件，并进行筛选
    :param current_file:指定目录下的文件名
    :return:包含txt文件的列表
    """
    txt_list = []    # 用列表储存txt文件的路径
    for names in current_file:    # 用变量存放文件地址，即文件夹名字加文件名称    
        if re.search(".txt", names, re.I):
            txt_list.append(names)
        else:
            pass
    return txt_list



distance_folder = ['48', '60', '72']
nozzles_folder = ['5nozzle', '3nozzle', '1nozzle']
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
txt_replace = '28.5-1.plt'
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
            file_names = os.listdir(dir_scale)
            txts = find_txt(file_names)
            for lays in txts:
                lay = open(dir_scale + '\\' + lays, "r", encoding="utf-8")
                file_data = ""
                txt_new = distance + '-' + str_factors + '.plt'
                for line in lay:
                    line = line.replace(txt_replace, txt_new)
                    file_data += line
                lay.close()
                lay_modified = open(dir_scale + '\\' + lays, "w", encoding="utf-8")
                lay_modified.write(file_data)
                lay_modified.close()
input("all done")