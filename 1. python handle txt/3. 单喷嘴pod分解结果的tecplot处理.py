import shutil
import os


print('定位后处理的目录')
onenozzlefolder = {'变当量比':'eq\\postprocessing\\', '变旋流数':'different swirl number\\postprocessing\\'}
folder = {'sw_folder': ["z-28.5", "z-35.5", "z-40.5", "z-45.5", "z-52.5"], 'eq_folder':["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]}
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
dir = 'E:\\0-PhD\\1 nozzle\\'
src_name = dir + 'POD速度分解结果的出图处理.lay'
data_src = '1-velocity.dat'
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
        dir_pod = dir_para + var + '\\pod_analyse\\'
        for scale in scale_factor:
            dst_name = dir_pod + str(scale)+'-velocity.lay'
            data_dst = str(scale)+'-velocity.dat'
            dst_name_txt = dst_name.strip('lay') + 'txt'
            shutil.copy(src_name, dst_name)
            os.rename(dst_name, dst_name_txt)
            with open(dst_name_txt, 'r+', encoding='utf-8') as f:
                content = f.read()
                content = content.replace(data_src, data_dst)
                f.seek(0,0)
                f.write(content)
                f.close()
            os.rename(dst_name_txt, dst_name)
input("tecplot处理导出完成")
