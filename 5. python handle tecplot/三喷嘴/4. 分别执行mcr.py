import os
import re
import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *

'''
把处理好的模板文件复制到各个文件夹下，然后再重新导出dat文件
'''


tp.session.connect()


def find_lay(current_file):
    lay_list = []    # 用列表储存txt文件的路径
    for names in current_file:
        if re.search(".lay", names, re.I):
            lay_list.append(names)
        else:
            pass
    return lay_list


if __name__ == "__main__":
    # 定义计算根目录
    dir_post = "E:\\0-PhD\\3 nozzle\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['1625','2250']
    sw_folder = ['388', '438', '508']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    # 
    print('# 找到工作目录')
    # 
    for distance in distance_folder:
        # G:\\assassin\\3nozzle\\1625
        dir_post_d = dir_post + distance
        mcrfile = dir_post_d + '\\change.mcr'
        # 变间距目录
        for sw in sw_folder:
            # G:\\assassin\\3nozzle\\1625\\388
            dir_post_sw = dir_post_d + '\\' + sw
            # 变缩比目录
            for num in range(len(scale_factor)):
                str_factors = str(scale_factor[num])
                # 后处理目录
                dir_post_working = dir_post_sw + '\\' + str_factors + '\\'
                print(dir_post_working)
                file = find_lay(os.listdir(dir_post_working))
                for lay in file:
                    print(dir_post_working+lay + 'is on processing')
                    try:
                        tp.load_layout(dir_post_working+lay)
                        tp.macro.execute_command('$!RedrawAll')
                        tp.macro.execute_file(mcrfile)
                        tp.save_layout(dir_post_working+lay, use_relative_paths=True)
                    except:
                        pass
print('all done')