# _*_ encoding utf-8 _*_
# 将想要的数据归到一个工作表里并保存

import xlwings as xw
 

def choosing():
    print(head_dic)
    action_str = input("选择想要的物理量：")
    action_str_int = int(action_str)
    if action_str_int in head_list:
        return action_str_int
    else:
        print("输入错误，请重新输入")
        choosing()




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
try:
    action_str_int = choosing()
except:
    print("\n输入错误, 请重新输入")
    action_str_int = choosing()
# 定义文件目录
eq_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# 定义统计物理量的目录以及建立统计表
for folders in eq_folder:
    str_folders = str(folders)
    dir_colletion = 'F:\\PhD\\1 nozzle\\eq\\postprocessing\\' + str_folders
    print(dir_colletion + ' is on processing')
    app_col = xw.App(visible=True, add_book=False)
    wb_collection = app_col.books.add()
    for i in range(1,5):
        i = 5-i
        wb_collection.sheets.add('POSITION' + str(i))
# 定义已有结果的目录
    for num in range(len(scale_factor)):
        factors = scale_factor[num]
        str_factors = str(factors)  
        dir_position = 'F:\\PhD\\1 nozzle\\eq\\postprocessing\\' + str_folders + '\\' + '40.5-' + str_factors
        print(str_folders + '-' + str_factors + ' is on going')
        app_ori = xw.App(visible=False, add_book=False)
        wb_ori = app_ori.books.open(dir_position+ '/' + "数值模拟结果整理.xls")
        num_inverse = 9-num
# 循环把四个特征位置的物理量都复制过去
        for i in range(0,4):
            sht_col = wb_collection.sheets[i]
            sht_ori = wb_ori.sheets[i]
# 定义读取数据的范围
            start = sht_dic[action_str_int] + '1'
            end = sht_dic[action_str_int] + '201'
            total = start + ':' + end
            my_data = sht_ori.range(total).value
            print(my_data)
# 定义导出数据的范围
            start = sht_dic[num_inverse] + '1'
            end = sht_dic[num_inverse] + '201'
            total = start + ':' + end
            sht_col.range(total).options(transpose=True).value = my_data
        app_ori.quit()
# 保存文件
    wb_collection.save(dir_colletion+ '/' + 'z-' + str_folders + '-' + head_dic[action_str_int] + ".xlsx")
    app_col.quit()

input("all done")