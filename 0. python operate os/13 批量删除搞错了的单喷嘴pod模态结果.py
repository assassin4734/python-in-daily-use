import shutil
import os
import re


print('定位后处理的目录')
onenozzlefolder = {'变当量比': 'eq\\postprocessing\\',
                   '变旋流数': 'different swirl number\\postprocessing\\'}
folder = {'sw_folder': ["z-28.5", "z-35.5", "z-40.5", "z-45.5", "z-52.5"],
          'eq_folder': ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]}
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
        # 把dat文件重名为txt然后修改内容，再改回来
        for file in files:
            if re.search("th_mode.lay", file, re.I):
                file_dat.append(file)
        for pod_dat in file_dat:
            os.remove(dir_pod + pod_dat)
input("删除完成")
