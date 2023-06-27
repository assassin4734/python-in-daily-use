import os
import re
import cv2
import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *


tp.session.connect(port=7600)


print('定位后处理的目录')
onenozzlefolder = {'变当量比': 'eq\\postprocessing-transport\\',
                   '变旋流数': 'different swirl number\\postprocessing\\'}
folder = {'sw_folder': ["z-28.5", "z-35.5", "z-45.5", "z-52.5"],
          'eq_folder': ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]}
scale_num = range(0, 7)
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
        # E:\\0-PhD\\1 nozzle\\eq\\postprocessing\\eq=0.55\\pod_analyse\\'
        dir_pod = dir_para + var + '\\pod_analyse\\pod_results\\'
        file_dat = []
        files = os.listdir(dir_pod)
        for lay in files:
            if re.search(".lay", lay, re.I):
                dir_lay = dir_pod + lay
                tp.macro.execute_command('$!RedrawAll')
                tp.load_layout(dir_lay)
                if lay == '1th_mode.lay':
                    tp.active_frame().plot().streamtraces.color=Color.Blue
                elif lay == '2th_mode.lay':
                    tp.active_frame().plot().streamtraces.color=Color.Custom32
                else:
                    pass
                ph = dir_lay.strip('.lay')+'.tiff'
                tp.export.save_tiff(ph,
                    width=1642,
                    region=ExportRegion.AllFrames,
                    supersample=1,
                    convert_to_256_colors=False,
                    gray_scale_depth=None,
                    byte_order=TIFFByteOrder.Intel)
                print(ph + ' photo exported')
                # 裁剪图片
                image_cut = cv2.imread(ph)
                size = image_cut.shape[0:3]
                image_cut = image_cut[21:511, 129:1610]
                cv2.imwrite(ph, image_cut)
                cv2.destroyAllWindows()
input("tecplot完成")
