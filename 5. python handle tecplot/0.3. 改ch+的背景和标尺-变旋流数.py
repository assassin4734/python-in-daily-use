import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *


tp.session.connect(port=7600)
# 定义目录
eq_folder = ["28.5", "35.5", "40.5", "45.5", "52.5"]
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
layouts = ['dimensionless ch+.lay']
for folders in eq_folder:
    # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55
    dir_colletion = 'E:\\0-PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + folders
    print(dir_colletion + ' is on processing')
    for factors in scale_factor:
        str_factors = str(factors)
        # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55\\40.5-1
        dir_position = dir_colletion + '\\' + folders + '-' + str_factors
        for lays in layouts:
            # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55\\40.5-1\\z-28.5-1-velocity.lay
            dir_final = dir_position + '\\' + lays
            print(dir_final + ' is on going')
            tp.load_layout(dir_final)
            tp.macro.execute_command('$!RedrawAll')
            tp.macro.execute_command('$!RedrawAll')
            tp.macro.execute_command("""$!CreateColorMap 
            Name = 'Modified Rainbow - Dark ends modified (1)'
            SourceColorMap = 'Modified Rainbow - Dark ends'""")
            tp.active_frame().plot().contour(0).colormap_name='Modified Rainbow - Dark ends modified (1)'
            tp.macro.execute_command("$!ColorMapAttributes 'Modified Rainbow - Dark ends modified (1)' ControlPoint 1 {LeadRGB{B = 0}}")
            tp.macro.execute_command("$!ColorMapAttributes 'Modified Rainbow - Dark ends modified (1)' ControlPoint 1 {TrailRGB{B = 0}}")
            tp.active_frame().plot().contour(0).levels.reset_to_nice(num_levels=9)
            tp.active_frame().plot().show_edge=False
            tp.macro.execute_command('$!RedrawAll')
            tp.save_layout(dir_final, use_relative_paths=True)
input("all done")


