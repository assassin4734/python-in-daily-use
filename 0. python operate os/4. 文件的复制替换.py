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


template_folder = [28.5, 35.5, 40.5, 45.5, 52.5]
eq_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
layouts = ['-velocity.lay', '-flame.lay', '-ch+.lay']
# 定义统计物理量的目录以及建立统计表
for lays in range(len(layouts)):
    for folders in template_folder:
        str_folders = str(folders)
        dir_colletion = 'F:\\PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders
        print(str_folders + ' is on processing')
    # 定义已有结果的目录
        for num in range(len(scale_factor)):
            factors = scale_factor[num]
            str_factors = str(factors)
            for eqs in range(len(eq_folder)):
                try:
                    template_position = 'F:\\PhD\\1 nozzle\\different swirl number\\postprocessing\\z-' + str_folders + '\\' + str_folders + '-' + str_factors + '\\' + 'z-28.5-1' + layouts[lays]
                    print(template_position)
                    eq_position = 'F:\\PhD\\1 nozzle\\eq\\postprocessing\\' + eq_folder[eqs] + '\\' + '40.5' + '-' + str_factors
                    print(eq_position)
                    copyFile(template_position, eq_position)
                except:
                    continue
input("all done")