import os


print('定位后处理的目录')
onenozzlefolder = {'变当量比': 'eq\\postprocessing-transport\\',
                   '变旋流数': 'different swirl number\\postprocessing\\'}
folder = {'sw_folder': ["z-28.5", "z-35.5", "z-40.5", "z-45.5", "z-52.5"],
          'eq_folder': ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]}
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
ch2obase = ['0.000260762', '0.000426918', '0.000510486', '0.000556973', '0.000578826']
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
                ch2o_d = ch2obase[folder[fol].index(var)]
                ch2o = "$!AlterData\n  Equation = '{CH2O}=V4/" + ch2o_d + "'\n"
            elif para == '变旋流数':
                third_fol = var.strip('z-') + '-' + str(scale)
                ch2o_d = ch2obase[1]
                ch2o = "$!AlterData\n  Equation = '{CH2O}=V4/" + ch2o_d + "'\n"
            else:
                pass
            dir_scale = dir_fol + third_fol + '\\z-28.5-1-ch+.txt'
            # os.remove(dir_scale)
            dir_scale_newch = dir_fol + third_fol + '\\dimensionless ch+.txt'
            # os.remove(dir_scale_newch)
            print(dir_scale + '正被处理\n')
            with open(dir_scale, 'r+', encoding='utf-8') as f:
                content = f.readlines()
                content.insert(231,ch2o)
                f.close()
            g = open(dir_scale_newch, 'w')
            g.writelines(content)
            g.close()
            os.rename(dir_scale_newch, dir_scale_newch.strip('txt')+'lay')
input("all done")