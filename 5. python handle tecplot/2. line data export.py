import tecplot as tp
import os
from tecplot.exception import *
from tecplot.constant import *




tp.session.connect(port=7600)

file_folder = [28.5, 35.5, 40.5, 45.5, 52.5]
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

for folders in file_folder:
  for factors in scale_factor:

    str_folders = str(folders)
    str_factors = str(factors)
    
    dir_working = 'F:\\PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders + '\\' + str_folders + '-' + str_factors + '\\z-28.5-1-velocity.lay'
    tp.load_layout(dir_working)
    dir_position = 'F:\\PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders + '\\' + str_folders + '-' + str_factors

    print(str_folders + '-' + str_factors + ' is on going')

    position1_com = "'XSTART = 0.333333 YSTART = -1.5 ZSTART = 0 XEND = 0.333333 YEND = 1.5 ZEND = 0 NUMPTS = 200 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = T EXTRACTFILENAME = " + "\\'" + dir_position  + "\\POSITION1.txt\\' '"
    position2_com = "'XSTART = 0.666667 YSTART = -1.5 ZSTART = 0 XEND = 0.666667 YEND = 1.5 ZEND = 0 NUMPTS = 200 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = T EXTRACTFILENAME = " + "\\'" + dir_position  + "\\POSITION2.txt\\' '"
    position3_com = "'XSTART = 1.33333 YSTART = -1.5 ZSTART = 0 XEND = 1.33333 YEND = 1.5 ZEND = 0 NUMPTS = 200 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = T EXTRACTFILENAME = " + "\\'" + dir_position + "\\POSITION3.txt\\' '"
    position4_com = "'XSTART = 2 YSTART = -1.5 ZSTART = 0 XEND = 2 YEND = 1.5 ZEND = 0 NUMPTS = 200 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = T EXTRACTFILENAME = " + "\\'" + dir_position + "\\POSITION4.txt\\' '"
    
    file_dir = dir_position + "\\export.txt"
    file_com = open(file_dir,'w')
    # file_com.write("")
    file_com.write("#!MC 1410\n$!RedrawAll\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = " + position1_com + "\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = " + position2_com + "\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = "  + position3_com + "\n$!ExtendedCommand\n  CommandProcessorID = 'Extract Precise Line'\n  Command = " + position4_com)
    file_com.close()
    portion = os.path.splitext(file_dir)
    newname = portion[0] + "2.mcr"
    os.rename(file_dir, newname)
    file_dir2 = dir_position + "\\export2.mcr"

    tp.macro.execute_file(file_dir2)


input("all done, press enter to exit")


