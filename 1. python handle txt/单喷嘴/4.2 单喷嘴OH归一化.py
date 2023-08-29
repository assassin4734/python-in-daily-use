import os
import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *


tp.session.connect(port=7600)


print('定位后处理的目录')
onenozzlefolder = {'变当量比': 'eq\\postprocessing-transport\\',
                   '变旋流数': 'different swirl number\\postprocessing\\'}
folder = {'sw_folder': ["z-28.5", "z-35.5", "z-45.5", "z-52.5"],
          'eq_folder': ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]}
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
ohbase_eq = ['0.000374318', '0.00143009', '0.00246363', '0.00313996', '0.00338699']
ohbase_sw = ['0.00113446', '0.0013674', '0.00122263', '0.00155205']
dir = 'E:\\0-PhD\\1 nozzle\\'
for para in onenozzlefolder:
    # E:\\0-PhD\\1 nozzle\\eq\\postprocessing\\
    dir_para = dir + onenozzlefolder[para]
    print(dir_para + '正被处理')
    if para == '变当量比':
        fol = 'eq_folder'
    elif para == '变旋流数':
        fol = 'sw_folder'
    else:
        pass
    for var in folder[fol]:
        # E:\\0-PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55\\
        dir_fol = dir_para + var + '\\'
        for scale in scale_factor:
            if para == '变当量比':
                third_fol = str(scale)
                OH_d = ohbase_eq[folder[fol].index(var)]
                OH_f = "$!AlterData\n  Equation = '{oh}=V13/" + OH_d + "'\n"
            elif para == '变旋流数':
                third_fol = var.strip('z-') + '-' + str(scale)
                OH_d = ohbase_sw[folder[fol].index(var)]
                OH_f = "$!AlterData\n  Equation = '{oh}=V13/" + OH_d + "'\n"
            else:
                pass
            dir_scale = dir_fol + third_fol + '\\z-28.5-1-ch+.txt'
            # os.remove(dir_scale)
            dir_scale_newoh = dir_fol + third_fol + '\\dimensionless OH.txt'
            if os.path.exists(dir_scale_newoh.strip('txt')+'lay') == True:
                os.remove(dir_scale_newoh.strip('txt')+'lay')
            # os.remove(dir_scale_newch)
            print(dir_scale + '正被处理\n')
            with open(dir_scale, 'r+', encoding='utf-8') as f:
                content = f.readlines()
                content.insert(231,OH_f)
                f.close()
            g = open(dir_scale_newoh, 'w')
            g.writelines(content)
            g.close()
            os.rename(dir_scale_newoh, dir_scale_newoh.strip('txt')+'lay')
            tp.load_layout(dir_scale_newoh.strip('txt')+'lay')
            tp.macro.execute_command('$!RedrawAll')
            tp.active_frame().plot().contour(0).variable_index=12
            tp.macro.execute_command("""$!CreateColorMap 
            Name = 'Modified Rainbow - Dark ends modified (1)'
            SourceColorMap = 'Modified Rainbow - Dark ends'""")
            tp.active_frame().plot().contour(0).colormap_name='Modified Rainbow - Dark ends modified (1)'
            tp.macro.execute_command("$!ColorMapAttributes 'Modified Rainbow - Dark ends modified (1)' ControlPoint 1 {LeadRGB{B = 0}}")
            tp.macro.execute_command("$!ColorMapAttributes 'Modified Rainbow - Dark ends modified (1)' ControlPoint 1 {TrailRGB{B = 0}}")
            tp.active_frame().plot().contour(0).levels.reset_to_nice(num_levels=19)
            tp.active_frame().plot().show_edge=False
            tp.macro.execute_command('$!RedrawAll')
            tp.save_layout(dir_scale_newoh.strip('txt')+'lay', use_relative_paths=True)
input("all done")