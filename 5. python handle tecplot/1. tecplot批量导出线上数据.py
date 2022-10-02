import tecplot as tp
import os
from tecplot.exception import *
from tecplot.constant import *


tp.session.connect(port=7600)

eq_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
line_position = ['0.333333', '0.666667', '1.33333', '2']
for folders in eq_folder:
    # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55
    dir_colletion = 'F:\\PhD\\1 nozzle\\eq\\postprocessing\\' + folders
    print(dir_colletion + ' is on processing')
    for factors in scale_factor:
        str_factors = str(factors)
        # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55\\40.5-1
        dir_position = dir_colletion + '\\40.5-' + str_factors
        # 定义导出地址
        pos = 0
        name_list = []
        while pos < 4:
            x_start = line_position[pos]
            pos += 1
            locals()['position' + str(pos) + '_com'] = "'XSTART = " + x_start + " YSTART = -1.5 ZSTART = 0 XEND = " + x_start + " YEND = 1.5 ZEND = 0 NUMPTS = 200 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = T EXTRACTFILENAME = " + "\\'" + dir_position  + "\\POSITION" + str(pos) + ".txt\\' '"
            name_list.append(locals()['position' + str(pos) + '_com'])
        file_dir = dir_position + "\\export.txt"
        file_com = open(file_dir,'w')
        # file_com.write("")
        file_com.write("#!MC 1410\n$!RedrawAll\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = " + name_list[0] + "\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = " + name_list[1] + "\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = "  + name_list[2] + "\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = " + name_list[3])
        file_com.close()
        portion = os.path.splitext(file_dir)
        newname = portion[0] + ".mcr"
        os.rename(file_dir, newname)
        file_dir2 = dir_position + "\\export.mcr"
        dir_layout = dir_position + "\\z-28.5-1-velocity.lay"
        tp.load_layout(dir_layout)
        tp.macro.execute_file(file_dir2)
        print(dir_position + ' has done')
input("all done, press enter to exit")