# -*- encoding utf-8 -*-
'''
向已有的excel表中写入公式
'''

import xlwings as xw
import string


sws = [28.5, 35.5, 40.5, 45.5, 52.5]
col = string.ascii_uppercase[0:22]
# 目录：E:\0-PhD\1 nozzle\different swirl number\postprocessing\
data_xls = ['无量纲轴向速度', '无量纲径向速度', 'turbulent-flame-speed']
app = xw.App(visible=True, add_book=False)
for sw in sws:
    dir_working = 'E:\\0-PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str(sw)
    for data in data_xls:
        dir_xls = dir_working + '\\' + 'z-' + str(sw) + '-' + data + '.xlsx'
        wb = app.books.open(dir_xls)
        for sheet_num in range(4):
            sht = wb.sheets[sheet_num]
            j = 1
            if data == 'turbulent-flame-speed':
                j = 12
            k = j + 10
            while j < k:
                sht.range((203,j)).value = '=MAX(' + col[j-1] + '2:' + col[j-1] + '201)'
                j += 1
            sht.range((203,k)).value = '最大值'
        wb.save(dir_xls)
        wb.close()

input('all done')
app.quit()