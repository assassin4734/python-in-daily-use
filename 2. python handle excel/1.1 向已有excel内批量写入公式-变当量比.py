# -*- encoding utf-8 -*-
'''
向已有的excel表中写入公式
'''

import xlwings as xw
import string


# 定义文件目录
eq_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# 定义统计物理量的目录以及建立统计表
for eq in eq_folder:
    # 地址格式举例：E:\\0-PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55
    dir_colletion = 'E:\\0-PhD\\1 nozzle\\eq\\postprocessing\\' + eq
    print(dir_colletion + ' is on processing')
    app = xw.App(visible=True, add_book=False)
    wb = app.books.open(dir_colletion + '\\turbulent-flame-speed.xlsx')
    factor_sht = wb.sheets['Sheet1']
    factor_sht['A1'].value = [50.35410629,45.31869566,40.28328503,35.2478744,30.21246377,25.17705314,20.14164252,15.10623189,10.07082126,5.035410629]
    col = string.ascii_uppercase[0:10]
    print(col)
    for k in range(4):
        sht = wb.sheets[k]
        j = 12
        while j < 22:
            i = 2
            while i < 202:
                sht.range((i,j)).value = '=' + col[j-12] + str(i) + '/Sheet1!' + col[j-12]+ '$1'
                i += 1
            j += 1
    wb.save(dir_colletion + '\\turbulent-flame-speed.xlsx')
    app.quit()
input("all done")