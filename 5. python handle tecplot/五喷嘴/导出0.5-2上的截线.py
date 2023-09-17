from tecplot.exception import *
from tecplot.constant import *
import tecplot as tp
import os


tp.session.connect()


def tecexport(dir_post_scale):
    dir_1 = dir_post_scale + 'plane-1.lay'
    dir_2 = dir_post_scale + 'plane-2.lay'
    dir_45 = dir_post_scale + 'plane-3.lay'
    dir_files = [dir_1, dir_2, dir_45]
    for i in range(len(dir_files)):
        lay = dir_files[i]
        tp.load_layout(lay)
        tp.macro.execute_command('$!RedrawAll')
        if i != 2:
            tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
                                              command='XSTART = -3.9 YSTART = 0.5 ZSTART = 0 XEND = 3.9 YEND = 0.5 ZEND = 0 NUMPTS = 600 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = F ')
            tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
                                              command='XSTART = -3.9 YSTART = 1 ZSTART = 0 XEND = 3.9 YEND = 1 ZEND = 0 NUMPTS = 600 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = F ')
            tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
                                              command='XSTART = -3.9 YSTART = 1.5 ZSTART = 0 XEND = 3.9 YEND = 1.5 ZEND = 0 NUMPTS = 600 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = F ')
            tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
                                              command='XSTART = -3.9 YSTART = 2 ZSTART = 0 XEND = 3.9 YEND = 2 ZEND = 0 NUMPTS = 600 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = F ')
        else:
            tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
                                              command='XSTART = -3 YSTART = 0.5 ZSTART = 0 XEND = 3 YEND = 0.5 ZEND = 0 NUMPTS = 400 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = F ')
            tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
                                              command='XSTART = -3 YSTART = 1 ZSTART = 0 XEND = 3 YEND = 1 ZEND = 0 NUMPTS = 400 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = F ')
            tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
                                              command='XSTART = -3 YSTART = 1.5 ZSTART = 0 XEND = 3 YEND = 1.5 ZEND = 0 NUMPTS = 400 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = F ')
            tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
                                              command='XSTART = -3 YSTART = 2 ZSTART = 0 XEND = 3 YEND = 2 ZEND = 0 NUMPTS = 400 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = F ')

        tp.macro.execute_command('$!RedrawAll')
        for j in range(4):
            zone = "[" + str(j+2) + "]"
            # os.remove(dir_post_scale + str((j+1)*0.25) + "-" + lay[-11:-4] + ".csv")
            dir_zone = dir_post_scale + str((j+1)*0.5) + "-" + lay[-11:-4] + ".csv"
            command_e_as_f = 'VarNames:FrOp=1:ZnCount=1:ZnList='+zone+':AllVars:ValSep=",":FNAME="'+dir_zone+'"'
            tp.macro.execute_extended_command(command_processor_id='excsv',
                                            command=command_e_as_f)
            print(dir_zone + '导出完成')


if __name__ == "__main__":
    # 定义计算根目录
    dir = "E:\\0-PhD\\5 nozzle\\0-5NOZZLE-DLN2.6SIZE\\"
    dir_post = dir + "postprocessing\\"
    # 定义目录变量
    nozzle_folder = ['5nozzle', '3nozzle', '1nozzle']
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
