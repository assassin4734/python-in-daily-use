from tecplot.exception import *
from tecplot.constant import *
import tecplot as tp


tp.session.connect()


def tecexport(dir_post_scale):
    dir_3 = dir_post_scale + 'flame-1.lay'
    dir_4 = dir_post_scale + 'flame-2.lay'
    dir_files = [dir_3, dir_4]
    for i in range(len(dir_files)):
        lay = dir_files[i]
        tp.load_layout(lay)
        tp.macro.execute_command('$!RedrawAll')
        tp.macro.execute_file('E:\\0-PhD\\5 nozzle\\0-5NOZZLE-DLN2.6SIZE\\postprocessing\\5nozzle\\48\\48-1\\polyline.mcr')
        tp.save_layout(lay, use_relative_paths=True)


if __name__ == "__main__":
    # 定义计算根目录
    dir = "E:\\0-PhD\\5 nozzle\\0-5NOZZLE-DLN2.6SIZE\\"
    dir_post = dir + "postprocessing\\"
    # 定义目录变量
    nozzle_folder = ['1nozzle', '3nozzle', '5nozzle']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    #
    print('# 找到工作目录')
    #
    for num1 in range(len(nozzle_folder)):
        # G:\\assassin\\3nozzle\\1625
        nozzle = nozzle_folder[num1]
        dir_post_n = dir_post + nozzle + '\\48\\48-'
        for num2 in range(len(scale_factor)):
            # 定义缩放因子对的变量和目录
            str_factors = str(scale_factor[num2])
            size = str(0.096*scale_factor[num2])
            dir_post_scale = dir_post_n + str_factors + '\\'
            print(dir_post_scale + ' 正在处理')
            tecexport(dir_post_scale)