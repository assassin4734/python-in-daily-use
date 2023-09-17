import cv2
import re
import os


def cutph(dir_post_sw_f, cutleft, cutright):
    for num2 in range(len(scale_factor)):
        str_factors = str(scale_factor[num2])
        dir_post = dir_post_sw_f + str_factors + '\\'
        # 后处理地址
        files = os.listdir(dir_post)
        ph_names = []
        for file in files:
            if re.search('.png', file, re.I) and file!='central-streamline.png' and file!='central-streamline-cut.png' and 'cut' not in file:
                ph_names.append(file)
        for ph_name in ph_names:
            dir_post_working = dir_post + ph_name
            print(dir_post_working)
            newimg = dir_post_working.replace(".png", "-cut.png")
            try:
                os.remove(newimg)
            except:
                print('no cut image exist')
                pass
            image_cut = cv2.imread(dir_post_working)
            print(dir_post_working)
            image_cut = image_cut[0:1770, cutleft:cutright]
            cv2.imwrite(newimg, image_cut)
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
            if distance == '1625':
                cutl = 173
                cutr = 3840
            elif distance == '2250':
                cutl = 252
                cutr = 5316
            cutph(dir_post_sw, cutl, cutr)
        else:
            cutl = 213
            cutr = 4550
            swfolder = ['388', '438', '508']
            for sw in swfolder:
                dir_post_sw = dir_post_d + '\\' + sw + '\\'
                cutph(dir_post_sw, cutl, cutr)
print('all done')
