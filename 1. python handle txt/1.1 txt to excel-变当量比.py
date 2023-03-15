# _*_ encoding utf-8 _*_
# 将txt文件转为xls格式

import os
import xlwt
import re


def change(current_file):
    """
    将指定文件夹目录下的txt转化为xls
    :param current_file:指定目录下的文件名
    :return:无
    """
    file_path = dir_position + '/' + current_file  # 用变量存放文件地址，即文件夹名字加文件名称
    txt0_file = open(file_path, 'r', encoding='gbk')    # 打开文件
    sheet = xls.add_sheet(current_file.strip('.Ttxt'),
                          cell_overwrite_ok=True)  # 增加工作表的表单
    row = 0  # 行数的计数器归零
    while True:
        line = txt0_file.readline()     # 逐行读取文件
        if not line:    # 结束读取跳出循环
            break
        txt_line = line.split()        # 获得单行由空格分隔的元组
        text_line_convert = []    # 保证数字格式，新建一个元组保存转换后的数字
        print(txt_line)
        for text in txt_line:    # 保证数字格式的循环建表
            try:
                text = float(text)
            except:
                pass
            text_line_convert.append(text)
        print(text_line_convert)
        for rank in range(len(text_line_convert)):        # 遍历元组进行操作，记录列数
            item = text_line_convert[rank]
            sheet.write(row, rank, item)            # 将元素写入表单
        row += 1        # 循环内计数器加一，转到下一行

    txt0_file.close()    # 关闭当前的txt文件
    # 添加表头
    line_head = ("CoordinateX", "CoordinateY", "CoordinateZ", "ch2o", "Turbulent Energy Dissipation", "turbulent-flame-speed", "X Component Vorticity", "Temperature", "Y Component Vorticity", "stretch-fac", "helicity", "Z Component Vorticity", "oh", "X Component Velocity", "Pressure",
                 "Y Component Velocity", "Turbulent Kinetic Energy", "fmean", "Z Component Velocity", "premixc", "damkohler-number", "Magnitude Vorticity", "turb-intensity", "heat-release-rate", "Magnitude Velocity", "q-criterion", "raw-q-criterion", "无量纲Z", "无量纲Y", "轴向速度", "径向速度")
    for elements in range(len(line_head)):
        head = line_head[elements]
        sheet.write(0, elements, head)
    xls.save(dir_position + '/' + "数值模拟结果整理-火焰.xls")    # 将对应的xls文件存储


def find_txt(current_file):
    """
    采用正则表达式判断当前目录下是否有txt文件，并进行筛选
    :param current_file:指定目录下的文件名
    :return:包含txt文件的列表
    """
    txt_list = []    # 用列表储存txt文件的路径
    xls_list = []
    for names in current_file:    # 用变量存放文件地址，即文件夹名字加文件名称
        if re.search("数值模拟结果整理-火焰.xls", names, re.I):
            xls_list.append(names)
            break
    if xls_list == []:
        for names in current_file:
            if re.search(".txt", names, re.I):
                if re.search("POSITION-F", names, re.I):
                    txt_list.append(names)
                else:
                    pass
    else:
        print("all data had been transferred")
    numbers_of_txt_in = len(txt_list)
    return txt_list, numbers_of_txt_in


eq_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# 建立工作目录
for folders in eq_folder:
    # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55
    dir_colletion = 'E:\\0-PhD\\1 nozzle\\eq\\postprocessing\\' + folders
    print(dir_colletion + ' is on processing')
    for factors in scale_factor:
        str_factors = str(factors)
        global dir_position
        # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55\\40.5-1
        dir_position = dir_colletion + '\\' + '40.5-' + str_factors
        print(dir_position + ' is on going')
        file_names = os.listdir(dir_position)   # 列举目录下文件
        txt_file_and_numbers = find_txt(file_names)
        txt_file = txt_file_and_numbers[0]
        numbers_of_txt = txt_file_and_numbers[1]
        if txt_file:    # 进行处理
            xls = xlwt.Workbook()  # 建立一个工作表
            for files in txt_file:
                change(files)
            number_convert = len(txt_file)
            print("\n转换完毕！共转换了%d个文件" % number_convert)

input("输入回车退出")
