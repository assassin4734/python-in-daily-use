import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *


tp.session.connect(port=7600)
# 定义目录
eq_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# layouts = ['dimensionless OH-cutregion.lay', 'dimensionless ch+.lay', 'z-28.5-1-flame.lay', 'z-28.5-1-velocity.lay']
layouts = ['z-28.5-1-flame.lay']
for folders in eq_folder:
    # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55
    dir_colletion = 'E:\\0-PhD\\1 nozzle\\eq\\postprocessing-transport\\' + folders
    print(dir_colletion + ' is on processing')
    for factors in scale_factor:
        str_factors = str(factors)
        # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55\\40.5-1
        dir_position = dir_colletion + '\\' + str_factors
        for lays in layouts:
            # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55\\40.5-1\\z-28.5-1-velocity.lay
            dir_final = dir_position + '\\' + lays
            print(dir_final + ' is on going')
            photo_name = lays.strip('z-28.5-1-').replace('.lay','')
            dir_save = dir_position + '\\' + photo_name + '.tiff'
            tp.macro.execute_command('$!RedrawAll')
            tp.load_layout(dir_final)
            tp.export.save_tiff(dir_save,
                width=1642,
                region=ExportRegion.AllFrames,
                supersample=1,
                convert_to_256_colors=False,
                gray_scale_depth=None,
                byte_order=TIFFByteOrder.Intel)
            print(photo_name + ' photo exported')
input("all done")


