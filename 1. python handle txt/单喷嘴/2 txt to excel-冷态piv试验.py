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
    file_path = dir_save + '/' + current_file  # 用变量存放文件地址，即文件夹名字加文件名称
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
    line_head = ("X (mm)", "Y (mm)", "Z (mm)", "U (m/s)", "V (m/s)", "W (m/s)", "Speed (m/s)", "Vorticity", "U-std", "V-std", "W-std", "Speed-std", "Vorticity-std", "R:U'V'", "R:V'W'",
                 "R:U'W", "T:U'U'+V'V'+W'W'", "Flag", "V19", "V20", "无量纲Y坐标", "无量纲X坐标", "无量纲U速度", "无量纲V速度")
    for elements in range(len(line_head)):
        head = line_head[elements]
        sheet.write(0, elements, head)
    xls.save(dir_save + '/' + "冷态PIV试验整理.xls")    # 将对应的xls文件存储


def find_txt(current_file):
    """
    采用正则表达式判断当前目录下是否有txt文件，并进行筛选
    :param current_file:指定目录下的文件名
    :return:包含txt文件的列表
    """
    txt_list = []    # 用列表储存txt文件的路径
    xls_list = []
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


dir = "E:\\0-PhD\\1 nozzle\\z-experiment\\z-cold experiments\\PIV_data\\"
Z_folder = ["25", "30", "35", "40", "45"]
xz_folder = ["z-1", "z-2", "z-3", "z-4",
             "z-5", "z-6", "z-7", "z-8", "z-9", "z-10"]
cate = ["Z", "xz"]
# 建立工作目录
for folders in cate:
    # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55
    dir_colletion = dir + folders + "\\"
    print(dir_colletion + ' is on processing')
    if folders == "Z":
        file = Z_folder
    elif folders == "xz":
        file = xz_folder
    for fo in file:
        dir_save = dir_colletion + fo
        file_names = os.listdir(dir_save)   # 列举目录下文件
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
