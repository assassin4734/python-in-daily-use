import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *
import os


tp.session.connect(port=7600)
# 定义目录
dir = "E:\\0-PhD\\1 nozzle\\z-experiment\\z-cold experiments\\PIV_data\\"
Z_folder = ["25", "30", "35", "40", "45"]
xz_folder = ["z-1", "z-2", "z-3", "z-4",
             "z-5", "z-6", "z-7", "z-8", "z-9", "z-10"]
cate = ["Z", "xz"]
tecname = "\\速度分布处理-新.lay"
line_position = ['0.333333', '0.666667', '1.33333', '2']
for folders in cate:
    # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55
    dir_colletion = dir + folders + "\\"
    print(dir_colletion + ' is on processing')
    if folders == "Z":
        file = Z_folder
    elif folders == "xz":
        file = xz_folder
    for lay in file:
        dir_save = dir_colletion + lay
        dir_lay = dir_save + tecname
        # 定义导出地址
        pos = 0
        name_list = []
        while pos < 4:
            y_start = line_position[pos]
            pos += 1
            locals()['position' + str(pos) + '_com'] = "'XSTART = -1.5" + " YSTART = " + y_start + " ZSTART = 0 XEND = 1.5" + \
                " YEND = " + y_start + " ZEND = 0 NUMPTS = 200 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = T EXTRACTFILENAME = " + \
                "\\'" + dir_save + "\\POSITION-F" + str(pos) + ".txt\\' '"
            name_list.append(locals()['position' + str(pos) + '_com'])
        file_dir = dir_save + "\\export.txt"
        file_com = open(file_dir, 'w')
        file_com.write("#!MC 1410\n$!RedrawAll\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = " + name_list[0] + "\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = " + name_list[
                       1] + "\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = " + name_list[2] + "\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = " + name_list[3])
        file_com.close()
        portion = os.path.splitext(file_dir)
        newname = portion[0] + ".mcr"
        os.rename(file_dir, newname)
        file_dir2 = dir_save + "\\export.mcr"
        print(dir_lay + ' is on going')
        tp.macro.execute_command('$!RedrawAll')
        tp.load_layout(dir_lay)
        tp.macro.execute_file(file_dir2)
        print(dir_lay + ' has done')
input("all done")
