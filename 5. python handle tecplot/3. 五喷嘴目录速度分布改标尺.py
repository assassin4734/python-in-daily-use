# -*- encoding utf-8 -*-
'''
多目录下tecplot图片导出
'''


import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *


tp.session.connect(port=7600)
# 定义目录
distance_folder = ['48', '60', '72']
nozzles_folder = ['5nozzle', '3nozzle', '1nozzle']
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
quantities = ['velocity.lay']
error_dir = []
for nozzles in nozzles_folder:
    # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle
    dir_nozzles = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\' + nozzles
    print(dir_nozzles + ' is on processing')
    for distance in distance_folder:
        # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48
        dir_distance = dir_nozzles + '\\' + distance
        for num in range(len(scale_factor)):
            str_factors = str(scale_factor[num]) 
            #  E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48\\48-1
            dir_scale = dir_distance + '\\' + distance + '-' + str_factors
            for quantity in quantities:
                try:
                    dir_tec = dir_scale + '\\' + quantity
                    print(dir_tec + ' is on going')
                    tp.macro.execute_command('$!RedrawAll')
                    tp.load_layout(dir_tec)
                    tp.active_frame().plot().contour(0).levels.reset_levels([-0.3, -0.1, 0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5])
                    tp.macro.execute_command('$!RedrawAll')
                    tp.save_layout(dir_tec, use_relative_paths=True)
                except:
                    print(dir_tec + ' error')
                    error_dir.append(dir_tec)
                    continue
for tec in error_dir:
    print(tec)
input("all done")