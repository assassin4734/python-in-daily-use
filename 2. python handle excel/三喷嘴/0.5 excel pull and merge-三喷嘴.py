# -*- coding:utf-8 -*
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


def pulling(dir_post_sw_f):
    for num in range(len(scale_factor)):
        str_factors = str(scale_factor[num])
        # 后处理地址
        dir_post_working = dir_post_sw_f + \
            str_factors + '\\' + name
        print(dir_post_working + ' is on going')
        app_ori = xw.App(visible=True, add_book=False)
        wb_ori = app_ori.books.open(dir_post_working)
        sht_col = wb_collection.sheets[0]
        sht_ori = wb_ori.sheets[0]
    # 定义读取数据的范围
        start = sht_dic[action_str_int] + '1'
        end = sht_dic[action_str_int] + '201'
        total = start + ':' + end
        my_data = sht_ori.range(total).value
    # 定义导出数据的范围
        start = sht_dic[num] + '1'
        end = sht_dic[num] + '201'
        total = start + ':' + end
        sht_col.range(total).options(transpose=True).value = my_data
        app_ori.quit()


# 定义出编号的个数，用于判断物理量以及字典的key
head_list = list(range(0,31))
# 给出物理量
line_head = ("CoordinateX", "CoordinateY", "CoordinateZ", "ch2o", "Turbulent Energy Dissipation", "turbulent-flame-speed", "X Component Vorticity", "Temperature", "Y Component Vorticity", "stretch-fac", "helicity", "Z Component Vorticity", "oh", "X Component Velocity", "Pressure", "Y Component Velocity", "Turbulent Kinetic Energy", "fmean", "Z Component Velocity", "premixc", "damkohler-number", "Magnitude Vorticity", "turb-intensity", "heat-release-rate", "Magnitude Velocity", "q-criterion", "raw-q-criterion", "无量纲Z", "无量纲Y", "无量纲轴向速度", "无量纲径向速度")
# 定义物理量字典
head_dic = dict(zip(head_list, line_head))
# 定义出列号
sht_head = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE']
# 把编号和列号对应以便于自动输出
sht_dic = dict(zip(head_list, sht_head))
# 输入物理量，容错
action_str_int = choosing()
# 定义统计物理量的目录以及建立统计表
dir_post = "E:\\0-PhD\\3 nozzle\\postprocessing\\"
# 定义目录变量
distance_folder = ['1625', '1925', '2250']
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
name = 'interline.xlsx'
#
print('# 找到工作目录')
#
for num1 in range(len(distance_folder)):
    # G:\\assassin\\3nozzle\\1625
    distance = distance_folder[num1]
    dir_post_d = dir_post + distance
    # 变间距目录
    # G:\\assassin\\3nozzle\\1625\\388
    if distance != '1925':
        app_col = xw.App(visible=True, add_book=False)
        wb_collection = app_col.books.add()
        sw = '438'
        dir_post_sw = dir_post_d + '\\' + sw + '\\'
        pulling(dir_post_sw)
        # 保存文件
        wb_collection.save(dir_post_sw+head_dic[action_str_int]+".xlsx")
        app_col.quit()
    else:
        swfolder = ['388', '438', '508']
        for sw in swfolder:
            app_col = xw.App(visible=True, add_book=False)
            wb_collection = app_col.books.add()
            dir_post_sw = dir_post_d + '\\' + sw + '\\'
            pulling(dir_post_sw)
            # 保存文件
            wb_collection.save(dir_post_sw+head_dic[action_str_int]+".xlsx")
            app_col.quit()
input("all done")