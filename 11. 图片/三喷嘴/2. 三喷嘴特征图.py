import cv2
import os


def cutph(dir_post):
    files = os.listdir(dir_post)
    for file in files:
        if '.png' in file:
            dir_post_working = dir_post + file
            image_cut = cv2.imread(dir_post_working)
            size = image_cut.shape[0:3]
            print(size)
            image_cut = image_cut[110:6623, 250:3840]
            cv2.imwrite(dir_post_working.replace(".png", "-cut.png"), image_cut)
            cv2.destroyAllWindows()
        else:
            pass
    return('all done')


dir = 'E:\\0-PhD\\3 nozzle\\PICTURES_OF_CHAPTER5\\流动与火焰特征\\汇总\\'
cutph(dir)