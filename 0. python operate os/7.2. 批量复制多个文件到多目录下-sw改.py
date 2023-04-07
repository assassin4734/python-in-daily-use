# _*_ encoding utf-8 _*_


import shutil


def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
         print('Error: %s' % e.strerror)


# 定义目录以及处理数据的列表
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
sw_folder = ["z-28.5", "z-35.5", "z-40.5", "z-45.5", "z-52.5"]
layouts = ['z-28.5-1-velocity.lay', 'z-28.5-1-flame.lay', 'z-28.5-1-ch+.lay']
dir_ori = 'E:\\0-PhD\\1 nozzle\\eq\\postprocessing\\eq=0.65\\'
dir_dst = 'E:\\0-PhD\\1 nozzle\\different swirl number\\postprocessing\\'
for sw in sw_folder:
    dir_sw_new = dir_dst + sw + '\\'
    print(dir_sw_new + ' is on processing')
    for num in range(len(scale_factor)):
        str_factors = str(scale_factor[num]) 
        dir_eq_scale = dir_ori + '40.5-' + str_factors + '\\'
        dir_sw_new_scale = dir_sw_new + sw.strip('z-') + '-' + str_factors + '\\'
        for quantity in layouts:
            try:
                template_position = dir_eq_scale + quantity
                print('原始文件地址' + template_position)
                de_position = dir_sw_new_scale + quantity
                print('目标文件地址' + de_position)
                copyFile(template_position, de_position)
            except:
                continue
input("all done")