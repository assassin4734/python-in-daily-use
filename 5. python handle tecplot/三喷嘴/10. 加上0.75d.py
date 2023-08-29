import os
import shutil
from tecplot.exception import *
from tecplot.constant import *
import tecplot as tp
'''
把处理好的模板文件复制到各个文件夹下，然后再无量纲化，最后重新导出dat文件
'''


tp.session.connect()


def change(dir_post_sw_f):
    # 先修改好参数
    for num2 in range(len(scale_factor)):
        str_factors = str(scale_factor[num2])
        exams = ['1d-p.lay', '1d-q.lay', '1d-vorticity.lay']
        for exam in exams:
            # 后处理目录
            dir_post_working = dir_post_sw_f + '\\' + str_factors + '\\' + exam
            dir_075d = dir_post_working.replace('1d', '0.75d')
            copyFile(dir_post_working, dir_075d)
            # 导出区域
            print(dir_post_working + ' 已拷贝修改完成')


def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
         print('Error: %s' % e.strerror)


if __name__ == "__main__":
    # 定义计算根目录
    dir_post = "E:\\0-PhD\\3 nozzle\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['1625', '1925', '2250']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    #
    print('# 找到工作目录')
    #
    for num1 in range(len(distance_folder)):
        # G:\\assassin\\3nozzle\\1625
        distance = distance_folder[num1]
        # 定义间距
        x_d = str(int(distance)*0.001)
        dir_post_d = dir_post + distance
        # 变间距目录
        # G:\\assassin\\3nozzle\\1625\\388
        if distance != '1925':
            sw = '438'
            dir_post_sw = dir_post_d + '\\' + sw
            change(dir_post_sw)
        else:
            swfolder = ['388', '438', '508']
            for sw in swfolder:
                dir_post_sw = dir_post_d + '\\' + sw
                change(dir_post_sw)
print('all done')