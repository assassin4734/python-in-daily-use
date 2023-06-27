import os


if __name__ == "__main__":
    # 定义计算根目录
    dir_post = "C:\\Users\\Administrator\\Desktop\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['1625','1925','225']
    sw_folder = ['388', '438', '508']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    for distance in distance_folder:
        # G:\\assassin\\3nozzle\\1625
        dir_post_d = dir_post + distance
        # 变间距目录
        for sw in sw_folder:
            # G:\\assassin\\3nozzle\\1625\\388
            dir_post_sw = dir_post_d + '\\' + sw
            # 变缩比目录
            for num in range(len(scale_factor)):
                str_factors = str(scale_factor[num])
                # 后处理目录
                dir_post_working = dir_post_sw + '\\' + str_factors + '\\'
                print(dir_post_working)
                try:
                    os.remove(dir_post_working + '1d.plt')
                    os.rename(dir_post_working + '0.75d.plt', dir_post_working + '1d.plt')
                    os.rename(dir_post_working + 'central-2.plt', dir_post_working + '0.75d.plt')
                except:
                    pass