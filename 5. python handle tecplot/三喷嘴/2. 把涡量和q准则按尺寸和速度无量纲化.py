import os
import re


'''
改尺寸和速度
'''


def change(dir_post_sw_f):
    # 先修改好参数
    for num2 in range(len(scale_factor)):
        str_factors = str(scale_factor[num2])
        size = str(0.096*scale_factor[num2])
        model_velocity = str(velocity[num2])
        # 后处理目录
        lays = []
        files = os.listdir(dir_post_sw_f + '\\' + str_factors)
        for file in files:
            if '.lay' in file:
                lays.append(file)
        for lay in lays:
            dir_post_working = dir_post_sw_f + '\\' + str_factors + '\\' + lay
            laytxt = dir_post_working.replace('.lay', '.txt')
            os.rename(dir_post_working, laytxt)
            # 改内容
            file_data = ""
            open_txt = open(laytxt, "r", encoding="utf-8")
            for line in open_txt:
                line = line.replace("0.096", size)
                line = line.replace("28.43562", model_velocity)
                line = line.replace("1d-dat", "0.75d-dat")
                file_data += line
            open_txt.close()
            open_txt = open(laytxt, "w", encoding="utf-8")
            open_txt.write(file_data)
            open_txt.close()
            os.rename(laytxt, dir_post_working)
            # 导出区域
            print(dir_post_working + ' 已修改完成')


if __name__ == "__main__":
    # 定义计算根目录
    dir_post = "E:\\0-PhD\\3 nozzle\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['1625', '1925', '2250']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    velocity = [28.43562, 25.59206, 22.7485, 19.90494, 17.0614, 12.79603, 11.37425, 9.952468, 8.530687, 7.108905]
    #
    print('# 找到工作目录')
    #
    for num1 in range(len(distance_folder)):
        # G:\\assassin\\3nozzle\\1625
        distance = distance_folder[num1]
        # 定义间距
        x_d = str(int(distance)*0.001)
        dir_post_d = dir_post + distance
        # 变间距目录
        # G:\\assassin\\3nozzle\\1625\\388
        if distance != '1925':
            sw = '438'
            dir_post_sw = dir_post_d + '\\' + sw
            change(dir_post_sw)
        else:
            swfolder = ['388', '438', '508']
            for sw in swfolder:
                dir_post_sw = dir_post_d + '\\' + sw
                change(dir_post_sw)
print('all done')