# -*- encoding utf-8 -*-
'''
向已有的excel表中写入公式
'''

import xlwings as xw
import string


# 定义文件目录
distance_folder = ['48', '60', '72']
nozzles_folder = ['5nozzle', '3nozzle', '1nozzle']
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
# 定义统计物理量的目录以及建立统计表
for nozzles in nozzles_folder:
    # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle
    dir_colletion = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\' + nozzles
    print(dir_colletion + ' is on processing')
    for distance in distance_folder:
        # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48
        dir_post_distance = dir_colletion + '\\' + distance
        app = xw.App(visible=True, add_book=False)
        wb = app.books.open(dir_post_distance + '\\turbulent-flame-speed.xlsx')
        factor_sht = wb.sheets['Sheet1']
        factor_sht['A1'].value = [40.17478098,36.15730288,32.13982479,28.12234669,24.10486859,18.07865144,16.06991239,14.06117334,12.05243429,10.04369525]
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
        wb.save(dir_post_distance + '\\turbulent-flame-speed.xlsx')
        app.quit()
input("all done")