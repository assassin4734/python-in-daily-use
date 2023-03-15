import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *


tp.session.connect(port=7600)
# 定义目录
sw_folder = ["28.5", "35.5", "40.5", "45.5", "52.5"]
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
for sw in sw_folder:
    dir_colletion = 'E:\\0-PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + sw
    print(dir_colletion + ' is on processing')
    for factors in scale_factor:
        str_factors = str(factors)
        dir_position = dir_colletion + '\\' + sw + '-' + str_factors
        # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55\\40.5-1\\z-28.5-1-velocity.lay
        dir_final = dir_position + '\\z-28.5-1-velocity.lay'
        tp.macro.execute_command('$!RedrawAll')
        tp.load_layout(dir_final)
        tp.macro.execute_command('$!RedrawAll')
        tp.macro.execute_command('''$!CreateRectangularZone 
                                    IMax = 200
                                    JMax = 200
                                    KMax = 1
                                    X1 = 0
                                    Y1 = -1.6
                                    Z1 = 0
                                    X2 = 5
                                    Y2 = 1.6
                                    Z2 = 0
                                    XVar = 29
                                    YVar = 28''')
        tp.macro.execute_command('''$!Pick SetMouseMode
                                    MouseMode = Select''')
        tp.active_frame().plot().show_mesh = True
        tp.macro.execute_command('$!RedrawAll')
        tp.data.operate.interpolate_linear(source_zones=[0],
                                           destination_zone=1,
                                           variables=[29, 30])
        tp.macro.execute_command('$!RedrawAll')
        tp.data.save_tecplot_ascii(dir_colletion + '\\pod_analyse\\' + str_factors + '-velocity.dat',
                                   zones=[1],
                                   variables=[27, 28, 29, 30],
                                   include_text=False,
                                   precision=9,
                                   include_geom=False,
                                   include_data_share_linkage=True,
                                   use_point_format=True)
        tp.macro.execute_command('$!RedrawAll')
