# -*- encoding utf-8 -*-
import os


if __name__ == "__main__":
    # 定义计算根目录
    dir = 'G:\\calculations\\1-5nozzle-fullgridandcorexperiment\\'
    dir_post = dir + 'postprocessing2\\'
    # 定义目录变量
    distance_folder = ['48']
    operating_folder = ['1nozzle', '3nozzle', '5nozzle']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    # 工况目录
    for operates in operating_folder:
        dir_post_op = dir_post + operates
        for distance in distance_folder:
            dir_post_D = dir_post_op + '\\' + distance
            # 变缩比目录
            for num in range(len(scale_factor)):
                str_factors = str(scale_factor[num])
                dir_post_working = dir_post_D + '\\' + distance + '-' + str_factors
                files = os.listdir(dir_post_working)
                for file in files:
                    if '.plt' not in file:
                        try:
                            os.remove(dir_post_working + '\\' + file)
                        except:
                            pass
    # 结束
    input("all done, input enter to exit")