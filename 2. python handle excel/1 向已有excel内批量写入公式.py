import imp


# -*- encoding utf-8 -*-
'''
向已有的excel表中写入公式
'''

import xlwings as xw
import string


wb = xw.books.active
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
