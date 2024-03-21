import tecplot as tp
import os
from tecplot.exception import *
from tecplot.constant import *


tp.session.connect(port=7600)
# 定义目录
dir1 = r'E:\3-work\4-other\TAIHANG\6-simulation\6DOME\ground'
dir2 = r'E:\3-work\4-other\TAIHANG\6-simulation\6DOME\design'
dir3 = r'E:\3-work\4-other\TAIHANG\6-simulation\9DOME\ground'
dir4 = r'E:\3-work\4-other\TAIHANG\6-simulation\9DOME\design'
dir_all = [dir1, dir2, dir3, dir4]


for dir in dir_all:
    files = os.listdir(dir)
    for file in files:
        if '.lay' in file:
            dir_lay = dir + '\\' + file
            dir_save = dir_lay.replace('.lay', '.tiff')
            tp.macro.execute_command('$!RedrawAll')
            tp.load_layout(dir_lay)
            tp.export.save_tiff(dir_save,
                width=1642,
                region=ExportRegion.AllFrames,
                supersample=1,
                convert_to_256_colors=False,
                gray_scale_depth=None,
                byte_order=TIFFByteOrder.Intel)
            print(dir_save + ' photo exported')
input("all done")


