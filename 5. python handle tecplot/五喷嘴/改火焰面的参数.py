import os
import re
import shutil
'''
把处理好的模板文件复制到各个文件夹下，然后再无量纲化
'''


def find_lay(current_file):
    lay_list = []    # 用列表储存txt文件的路径
    for names in current_file:
        if re.search(".lay", names, re.I) and ('plane' in names):
            lay_list.append(names)
        else:
            pass
    return lay_list


def change(files, dir_post_scale):
    # 先修改好参数
    for file in files:
        dir_file = dir_post_scale + file
        copyFile(dir_exam+file, dir_file)
        laytxt = dir_file.replace('.lay', '.txt')
        os.rename(dir_file, laytxt)
        # 改内容
        file_data = ""
        open_txt = open(laytxt, "r", encoding="utf-8")
        for line in open_txt:
            line = line.replace("0.096", size)
            line = line.replace("28.43562", model_velocity)
            line = line.replace("40.98", model_velocity)
            file_data += line
        open_txt.close()
        open_txt = open(laytxt, "w", encoding="utf-8")
        open_txt.write(file_data)
        open_txt.close()
        os.rename(laytxt, dir_file)
        print(dir_file + ' 已拷贝修改完成')


def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
         print('Error: %s' % e.strerror)


if __name__ == "__main__":
    # 定义计算根目录
    dir = "E:\\0-PhD\\5 nozzle\\0-5NOZZLE-DLN2.6SIZE\\"
    dir_post = dir + "postprocessing\\"
    dir_exam = dir + "example\\"
    files = find_lay(os.listdir(dir_exam))
    # 定义目录变量
    nozzle_folder = ['1nozzle', '3nozzle', '5nozzle']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    velocity = [40.98, 36.88, 32.78, 28.68, 24.59, 18.44, 16.39, 14.34, 12.29, 10.24]
    #
    print('# 找到工作目录')
    #
    for num1 in range(len(nozzle_folder)):
        # G:\\assassin\\3nozzle\\1625
        nozzle = nozzle_folder[num1]
        dir_post_n = dir_post + nozzle + '\\48\\48-'
        for num2 in range(len(scale_factor)):
            # 定义缩放因子对的变量和目录
            str_factors = str(scale_factor[num2])
            size = str(0.096*scale_factor[num2])
            model_velocity = str(velocity[num2])
            dir_post_scale = dir_post_n + str_factors + '\\'
            change(files, dir_post_scale)
print('all done')