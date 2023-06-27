import os
import re
import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *


'''
把处理好的模板文件复制到各个文件夹下，然后再重新导出dat文件
'''


def find_lay(current_file):
    lay_list = []    # 用列表储存txt文件的路径
    for names in current_file:
        if re.search(".lay", names, re.I):
            newname = names[:-4]
            lay_to_txt = dir_post_working + newname + '.txt'
            os.rename(dir_post_working+names, lay_to_txt)
            lay_list.append(lay_to_txt)
        else:
            pass
    return lay_list


if __name__ == "__main__":
    # 定义计算根目录
    dir_post = "E:\\0-PhD\\3 nozzle\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['1625','1925','2250']
    sw_folder = ['388', '438', '508']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    velocity = [28.43562, 25.59206, 22.7485, 19.90494, 17.0614, 12.79603, 11.37425, 9.952468, 8.530687, 7.108905]
    # 
    print('# 找到工作目录')
    # 
    for distance in distance_folder:
        # G:\\assassin\\3nozzle\\1625
        dir_post_d = dir_post + distance
        # 变间距目录
        for sw in sw_folder:
            # G:\\assassin\\3nozzle\\1625\\388
            dir_post_sw = dir_post_d + '\\' + sw
            # 变缩比目录
            for num in range(len(scale_factor)):
                str_factors = str(scale_factor[num])
                size = str(0.096*scale_factor[num])
                model_velocity = str(velocity[num])
                # 后处理目录
                dir_post_working = dir_post_sw + '\\' + str_factors + '\\'
                print(dir_post_working)
                file = find_lay(os.listdir(dir_post_working))
                for laytxt in file:
                    file_data = ""
                    open_txt = open(laytxt, "r", encoding="utf-8")
                    for line in open_txt:
                        line = line.replace("0.096", size)
                        line = line.replace("28.43562", model_velocity)
                        file_data += line
                    open_txt.close()
                    open_txt = open(laytxt, "w", encoding="utf-8")
                    open_txt.write(file_data)
                    open_txt.close()
                    oldname = laytxt[:-4]
                    os.rename(laytxt, oldname+'.lay')
print('all done')