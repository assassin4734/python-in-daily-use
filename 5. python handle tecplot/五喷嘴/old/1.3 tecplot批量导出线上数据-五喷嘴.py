import tecplot as tp
import os
from tecplot.exception import *
from tecplot.constant import *


tp.session.connect(port=7600)

# 定义目录变量
distance_folder = ['48', '60', '72']
nozzles_folder = ['5nozzle', '3nozzle', '1nozzle']
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
line_position = ['0.5', '1.5', '2.5', '3.5']
fail = []
# 定义一级目录
for nozzles in nozzles_folder:
    '''
    变量中间是fluent，就是说明这个变量是fluent的地址
    变量中间是post，就是说明这个变量是后处理的地址
    '''
    # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle
    dir_post_nozzles = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\' + nozzles
    print(dir_post_nozzles + ' is on processing')
    # 定义二级目录
    for distance in distance_folder:
        # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48
        dir_post_distance = dir_post_nozzles + '\\' + distance
        # 定义三级目录
        for num in range(len(scale_factor)):
            dir_position = dir_post_distance + '\\' + distance + '-' + str(scale_factor[num])
            # 定义导出地址
            pos = 0
            name_list = []
            while pos < 4:
                x_start = line_position[pos]
                pos += 1
                locals()['position' + str(pos) + '_com'] = "'XSTART = " + x_start + " YSTART = 0 ZSTART = 0 XEND = " + x_start + " YEND = 4 ZEND = 0 NUMPTS = 200 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = T EXTRACTFILENAME = " + "\\'" + dir_position  + "\\POSITION-F" + str(pos) + ".txt\\' '"
                name_list.append(locals()['position' + str(pos) + '_com'])
            file_dir = dir_position + "\\export20230306.txt"
            file_com = open(file_dir,'w')
            file_com.write("#!MC 1410\n$!RedrawAll\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = " + name_list[0] + "\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = " + name_list[1] + "\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = "  + name_list[2] + "\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = " + name_list[3])
            file_com.close()
            portion = os.path.splitext(file_dir)
            newname = portion[0] + ".mcr"
            os.rename(file_dir, newname)
            file_dir2 = dir_position + "\\export20230306.mcr"
            dir_layout = dir_position + "\\velocity.lay"
            try:
                tp.load_layout(dir_layout)
                tp.macro.execute_file(file_dir2)
                print(dir_position + ' has done')
            except:
                fail.append(dir_layout)
                continue
print('\n')
for ele in fail:
    print(ele)
input("all done, press enter to exit")