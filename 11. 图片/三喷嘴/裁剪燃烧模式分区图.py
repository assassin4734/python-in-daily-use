import cv2
import os


def cutph(dir_post):
    files = os.listdir(dir_post)
    for file in files:
        if '.PNG' in file:
            dir_post_working = dir_post + file
            os.rename(dir_post_working, dir_post_working.replace('幻灯片', ''))
            dir_post_working = dir_post_working.replace('幻灯片', '')
            print(dir_post_working)
            image_cut = cv2.imread(dir_post_working)
            image_cut = image_cut[109:2474, 0:2938]
            cv2.imwrite(dir_post_working.replace(".png", "-cut.png"), image_cut)
            cv2.destroyAllWindows()
        else:
            pass
    return('all done')


dir = 'E:\\0-PhD\\3 nozzle\\coldflowfield\\combustion regime\\regime\\'
cutph(dir)