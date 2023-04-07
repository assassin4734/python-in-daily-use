# -*- encoding utf-8 -*-
'''
将想要的数据归到一个工作表里并保存
'''


import xlwings as xw
import os


def choosing():
    print(head_dic)
    print("输入exit退出")
    action_str = input("选择想要的物理量：")
    try:
        if int(action_str) in head_list:
            return int(action_str)
        else:
            print("编号输入错误，请重新输入")
            choosing()
    except:
        if action_str == 'exit':
            os._exit(0)
        print("编号输入错误，请重新输入")
        choosing()


# 定义出编号的个数，用于判断物理量以及字典的key
head_list = list(range(0, 31))
# 给出物理量
line_head = ("X (mm)", "Y (mm)", "Z (mm)", "U (m/s)", "V (m/s)", "W (m/s)", "Speed (m/s)", "Vorticity", "U-std", "V-std", "W-std", "Speed-std", "Vorticity-std", "R:U'V'", "R:V'W'",
             "R:U'W", "T:U'U'+V'V'+W'W'", "Flag", "V19", "V20", "无量纲Y坐标", "无量纲X坐标", "无量纲U速度", "无量纲V速度")
# 定义物理量字典
head_dic = dict(zip(head_list, line_head))
# 定义出列号
sht_head = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
# 把编号和列号对应以便于自动输出
sht_dic = dict(zip(head_list, sht_head))
# 输入物理量，容错
action_str_int = choosing()
dir = "E:\\0-PhD\\1 nozzle\\z-experiment\\z-cold experiments\\PIV_data\\"
Z_folder = ["25", "30", "35", "40", "45"]
xz_folder = ["z-1", "z-2", "z-3", "z-4",
             "z-5", "z-6", "z-7", "z-8", "z-9", "z-10"]
cate = ["Z", "xz"]
# 建立工作目录
for folders in cate:
    dir_colletion = dir + folders + "\\"
    print(dir_colletion + ' is on processing')
    if folders == "Z":
        file = Z_folder
    elif folders == "xz":
        file = xz_folder
    app_col = xw.App(visible=True, add_book=False)
    wb_collection = app_col.books.add()
    for i in range(1, 5):
        i = 5-i
        wb_collection.sheets.add('POSITION' + str(i))
    for fo in file:
        dir_save = dir_colletion + fo
        print(dir_save + ' is on going')
        app_ori = xw.App(visible=False, add_book=False)
        wb_ori = app_ori.books.open(dir_save + '/' + "冷态PIV试验整理.xls")
# 循环把四个特征位置的物理量都复制过去
        for i in range(0, 4):
            sht_col = wb_collection.sheets[i]
            sht_ori = wb_ori.sheets[i]
# 定义读取数据的范围
            start = sht_dic[action_str_int] + '1'
            end = sht_dic[action_str_int] + '201'
            total = start + ':' + end
            my_data = sht_ori.range(total).value
# 定义导出数据的范围
            start = sht_dic[file.index(fo)] + '1'
            end = sht_dic[file.index(fo)] + '201'
            total = start + ':' + end
            sht_col.range(total).options(transpose=True).value = my_data
        app_ori.quit()
# 保存文件
    wb_collection.save(dir_colletion + '\\' +
                        head_dic[action_str_int] + ".xlsx")
    app_col.quit()

input("all done")
