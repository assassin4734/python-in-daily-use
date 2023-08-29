import cv2


def cutph(dir_post_sw_f):
    for num2 in range(len(scale_factor)):
        str_factors = str(scale_factor[num2])
        # 后处理地址
        dir_post_working = dir_post_sw_f + '\\' + \
            str_factors + '\\central-streamline.png'
        image_cut = cv2.imread(dir_post_working)
        size = image_cut.shape[0:3]
        print(size)
        image_cut = image_cut[110:6623, 250:3840]
        cv2.imwrite(dir_post_working.replace(".png", "-cut.png"), image_cut)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # 定义计算根目录
    dir_post = "E:\\0-PhD\\3 nozzle\\postprocessing\\"
    # 定义目录变量
    distance_folder = ['1625', '1925', '2250']
    scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
    #
    print('# 找到工作目录')
    #
    for num1 in range(len(distance_folder)):
        # G:\\assassin\\3nozzle\\1625
        distance = distance_folder[num1]
        dir_post_d = dir_post + distance
        # 变间距目录
        # G:\\assassin\\3nozzle\\1625\\388
        if distance != '1925':
            sw = '438'
            dir_post_sw = dir_post_d + '\\' + sw + '\\'
            cutph(dir_post_sw)
        else:
            swfolder = ['388', '438', '508']
            for sw in swfolder:
                dir_post_sw = dir_post_d + '\\' + sw + '\\'
                cutph(dir_post_sw)
print('all done')
