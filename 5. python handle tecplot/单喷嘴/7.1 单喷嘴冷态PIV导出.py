import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *


tp.session.connect(port=7600)
# 定义目录
dir = "E:\\0-PhD\\1 nozzle\\z-experiment\\z-冷态试验\\PIV冷态数据\\"
Z_folder = ["25", "30", "35", "40", "45"]
xz_folder = ["z-1", "z-2", "z-3", "z-4", "z-5", "z-6", "z-7", "z-8", "z-9", "z-10"]
cate = ["Z冷态PIV试验数据", "xz冷态PIV试验数据"]
tecname = "\\速度分布处理-新.lay"
for folders in cate:
    # 地址格式举例：F:\\PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55
    dir_colletion = dir + folders + "\\"
    print(dir_colletion + ' is on processing')
    if folders == "Z冷态PIV试验数据":
        file = Z_folder
    elif folders == "xz冷态PIV试验数据":
        file = xz_folder
    for lay in file:
        dir_save = dir_colletion + lay
        dir_lay = dir_save + tecname
        print(dir_lay + ' is on going')
        tp.macro.execute_command('$!RedrawAll')
        tp.load_layout(dir_lay)
        tp.export.save_tiff(dir_save+'.tiff',
            width=1642,
            region=ExportRegion.AllFrames,
            supersample=1,
            convert_to_256_colors=False,
            gray_scale_depth=None,
            byte_order=TIFFByteOrder.Intel)
        print(dir_lay + ' photo exported')
input("all done")