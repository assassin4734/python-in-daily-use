from tecplot.exception import *
from tecplot.constant import *
import tecplot as tp


tp.session.connect()


dir_post_scale1 = r'E:\0-PhD\5 nozzle\0-5NOZZLE-DLN2.6SIZE\postprocessing\5nozzle\48\48-1\y-velocity-1.lay'
print(dir_post_scale1 + ' 正在处理')
tp.load_layout(dir_post_scale1)
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
                                    command='XSTART = -2.5 YSTART = -0.918 ZSTART = 0 XEND = 0.5 YEND = -0.918 ZEND = 0 NUMPTS = 400 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = F ')
tp.macro.execute_command('$!RedrawAll')
dir_zone1 = r'E:\0-PhD\5 nozzle\0-5NOZZLE-DLN2.6SIZE\postprocessing\5nozzle\48\48-1\MF-1.csv'
zone = "[" + str(2) + "]"
command_e_as_f = 'VarNames:FrOp=1:ZnCount=1:ZnList='+zone+':AllVars:ValSep=",":FNAME="'+dir_zone1+'"'
tp.macro.execute_extended_command(command_processor_id='excsv',
                                    command=command_e_as_f)
print(dir_zone1 + '导出完成')
dir_post_scale2 = r'E:\0-PhD\5 nozzle\0-5NOZZLE-DLN2.6SIZE\postprocessing\5nozzle\48\48-0.25\y-velocity-1.lay'
print(dir_post_scale2 + ' 正在处理')
tp.load_layout(dir_post_scale2)
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
                                    command='XSTART = -2.5 YSTART = -0.918 ZSTART = 0 XEND = 0.5 YEND = -0.918 ZEND = 0 NUMPTS = 400 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = F ')
tp.macro.execute_command('$!RedrawAll')
dir_zone2 = r'E:\0-PhD\5 nozzle\0-5NOZZLE-DLN2.6SIZE\postprocessing\5nozzle\48\48-0.25\MF-0.25.csv'
zone = "[" + str(2) + "]"
command_e_as_f = 'VarNames:FrOp=1:ZnCount=1:ZnList='+zone+':AllVars:ValSep=",":FNAME="'+dir_zone2+'"'
tp.macro.execute_extended_command(command_processor_id='excsv',
                                    command=command_e_as_f)
print(dir_zone1 + '导出完成')
