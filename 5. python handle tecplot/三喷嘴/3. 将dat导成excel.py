# _*_ encoding utf-8 _*_
# 将txt文件转为xls格式

import os
import re
import pandas as pd
import numpy as np
import xlwings as xw


pd.set_option("mode.chained_assignment", None)


def change_and_cal(current_file):
    """
    将指定文件夹目录下的dat转化为xls
    :param current_file:指定目录下的文件名
    :return:无
    """
    file_path = dir_post_working + current_file  # 用变量存放文件地址，即文件夹名字加文件名称
    excelpath = file_path.strip('.dat')+'.xlsx'
    datexcel = pd.read_csv(file_path, sep=' ', dtype=np.float64, skiprows=44, names=["CoordinateX", "CoordinateY", "CoordinateZ", "ch2o", "Turbulent Energy Dissipation", "turbulent-flame-speed", "X Component Vorticity", "Temperature", "Y Component Vorticity", "stretch-fac", "helicity", "Z Component Vorticity",
                      "oh", "X Component Velocity", "Pressure", "Y Component Velocity", "Turbulent Kinetic Energy", "fmean", "Z Component Velocity", "premixc", "damkohler-number", "Magnitude Vorticity", "turb-intensity", "heat-release-rate", "Magnitude Velocity", "q-criterion", "raw-q-criterion", "无量纲X", "无量纲Y", "dimensionless z vorticity", "dimensionless Q"])
    datexcel.to_excel(excelpath)    # 将对应的xlsx文件存储
    datexcel = None
    if sw == '508' and scale_factor[num] == 1:
        print('# 启动用来计算最大值的excel')
        app_col = xw.App(visible=True, add_book=False)  
        wb = app_col.books.open(excelpath)  # 打开转换的excel
        sheet = wb.sheets['Sheet1']
        sheet["AE40002"].value = '=MAX(AE2:AE40001)'
        sheet["AF40002"].value = '=MAX(AF2:AF40001)'
        d_z_vor = sheet["AE40002"].value
        d_q = sheet["AF40002"].value
        wb.save(excelpath)
        app_col.quit()
        return d_z_vor, d_q
    else:
        pass


def find_dat(current_file):
    """
    采用正则表达式判断当前目录下是否有txt文件，并进行筛选
    :param current_file:指定目录下的文件名
    :return:包含txt文件的列表
    """
    dat_list = []    # 用列表储存txt文件的路径
    for names in current_file:
        if re.search(".dat", names, re.I):
            dat_list.append(names)
        else:
            pass
    numbers_of_dat_in = len(dat_list)
    return dat_list, numbers_of_dat_in


# 定义计算根目录
dir_post = "E:\\0-PhD\\3 nozzle\\postprocessing\\"
# 定义目录变量
distance_folder = ['1625', '1925', '2250']
sw_folder = ['388', '438', '508']
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
d_z_vor_list = []
d_q_list = []
for distance in distance_folder:
    # G:\\assassin\\3nozzle\\1625
    dir_post_d = dir_post + distance
    # 变间距目录
    for sw in sw_folder:
        # G:\\assassin\\3nozzle\\1625\\388
        dir_post_sw = dir_post_d + '\\' + sw
        # 变缩比目录
        for num in range(len(scale_factor)):
            str_factors = str(scale_factor[num])
            # 后处理目录
            dir_post_working = dir_post_sw + '\\' + str_factors + '\\'
            print(dir_post_working)
            print('# 列举目录下文件')
            file_names = os.listdir(dir_post_working)
            print('# 找到目标文件')
            dat_file_and_numbers = find_dat(file_names)
            dat_file = dat_file_and_numbers[0]
            numbers_of_txt = dat_file_and_numbers[1]
            print('# 开始转换')
            if dat_file:    # 进行处理
                for files in dat_file:
                    if sw == '508' and scale_factor[num] == 1:
                        d_z_vor_v, d_q_v = change_and_cal(files)
                        d_z_vor_list.append(d_z_vor_v)
                        d_q_list.append(d_q_v)
                    else:
                        change_and_cal(files)
                number_convert = len(dat_file)
                print("\n转换完毕！共转换了%d个文件" % number_convert)
print(d_z_vor_list)
print(d_q_list)
input("输入回车退出")
