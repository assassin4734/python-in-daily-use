import pandas as pd
import xlwings as xw
'''
把计算结果整合到一个excel里
'''


def coldflowfield(sw):
    '''
    读取各个文件夹下的数据然后整合
    '''
    # 定义计数器
    count = 0
    app = xw.App(visible=True, add_book=False)
    wb = app.books.add()
    sht = wb.sheets[0]
    for loc in range(len(scale_factor)):
        # 读取数据
        dir_cold_scale = dir_cold_d + '\\' + sw + '\\' + str(scale_factor[loc])
        # 合并单元格，输入几何模化因子
        sht[0,count+loc].value = str(scale_factor[loc])
        # sht.range('A1:B1').api.merge()
        # 读取该几何模化因子下的结果
        dir_data = dir_cold_scale + '\\计算完成的值.xlsx'
        ori = pd.read_excel(dir_data)
        x = list(ori['湍流尺度与层流火焰厚度之比'])
        print(x)
        y = list(ori['脉动速度和层流火焰传播速度之比'])
        print(y)
        # 把x和y赋值到列
        sht[1,count+loc].value = '湍流尺度与层流火焰厚度之比'
        sht[1,count+loc+1].value = '脉动速度和层流火焰传播速度之比'
        sht[2,count+loc].options(transpose=True).value = x
        sht[2,count+loc+1].options(transpose=True).value = y
        # 计数器加一
        count+=1
    wb.save(dir_cold_d + '\\' + sw + '\\燃烧模式数据整合.xlsx')
    app.quit()


if __name__ == "__main__":
    # 定义计算根目录
    dir_cold = "E:\\0-PhD\\3 nozzle\\coldflowfield\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['1925', '1625', '2250']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    #
    print('# 找到工作目录')
    #
    for di in range(len(distance_folder)):
        # G:\\assassin\\3nozzle\\1625
        distance = distance_folder[di]
        # 定义新目录
        dir_cold_d = dir_cold + distance
        # 变间距目录
        # G:\\assassin\\3nozzle\\1625\\388
        if distance != '1925':
            sw = '438'
            coldflowfield(sw)
        else:
            swfolder = ['388', '438', '508']
            for sw in swfolder:
                coldflowfield(sw)
print('全部完成')