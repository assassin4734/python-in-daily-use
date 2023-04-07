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
eq_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
layouts = ['z-28.5-1-velocity.lay', 'z-28.5-1-flame.lay', 'z-28.5-1-ch+.txt']
dir_ori = 'E:\\0-PhD\\1 nozzle\\eq\\postprocessing\\'
dir_dst = 'E:\\0-PhD\\1 nozzle\\eq\\postprocessing-transport\\'
for eq in eq_folder:
    dir_eq = dir_ori + eq + '\\'
    dir_eq_new = dir_dst + eq + '\\'
    print(dir_eq_new + ' is on processing')
    for num in range(len(scale_factor)):
        str_factors = str(scale_factor[num]) 
        dir_eq_scale = dir_eq + '40.5-' + str_factors + '\\'
        dir_eq_new_scale = dir_eq_new + str_factors + '\\'
        for quantity in layouts:
            try:
                template_position = dir_eq_scale + quantity
                print('原始文件地址' + template_position)
                de_position = dir_eq_new_scale + quantity
                print('目标文件地址' + de_position)
                copyFile(template_position, de_position)
            except:
                continue
input("all done")