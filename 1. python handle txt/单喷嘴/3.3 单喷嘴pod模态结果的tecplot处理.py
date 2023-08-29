import shutil
import os
import re


print('定位后处理的目录')
onenozzlefolder = {'变当量比': 'eq\\postprocessing-transport\\',
                   '变旋流数': 'different swirl number\\postprocessing\\'}
folder = {'sw_folder': ["z-28.5", "z-35.5", "z-45.5", "z-52.5"],
          'eq_folder': ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]}
scale_num = range(0, 10)
dir = 'E:\\0-PhD\\1 nozzle\\'
src_name = dir + 'POD速度分解结果的出图处理.lay'
data_src = '''VARIABLES = Z,Y,U,V
ZONE I=200,J=200,F=POINT'''
data_dst = '''TITLE     = "Tecplot Export"
VARIABLES = "V28"
"V29"
"V30"
"V31"
ZONE T="Rectangular zone"
 STRANDID=0, SOLUTIONTIME=0
 I=200, J=200, K=1, ZONETYPE=Ordered
 DATAPACKING=POINT
 DT=(SINGLE SINGLE SINGLE SINGLE )'''
txt_src = '1-velocity.dat'
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
            if re.search(".dat", file, re.I):
                file_dat.append(file)
        for pod_dat in file_dat:
            pod_dat_dir = dir_pod + pod_dat
            pod_txt = dir_pod + pod_dat.strip('dat') + 'txt'
            os.rename(pod_dat_dir, pod_txt)
            with open(pod_txt, 'r+', encoding='utf-8') as f:
                content = f.read()
                content = content.replace(data_src, data_dst)
                f.seek(0, 0)
                f.write(content)
                f.close()
            os.rename(pod_txt, pod_dat_dir)
        for scale in scale_num:
            dst_name = dir_pod + str(scale)+'th_mode.lay'
            shutil.copy(src_name, dst_name)
            lay_txt = dst_name.strip('lay') + 'txt'
            os.rename(dst_name, lay_txt)
            with open(lay_txt, 'r+', encoding='utf-8') as f:
                content = f.read()
                content = content.replace(txt_src, str(scale) + 'th_mode.dat')
                f.seek(0, 0)
                f.write(content)
                f.close()
            os.rename(lay_txt, dst_name)
input("tecplot完成")
