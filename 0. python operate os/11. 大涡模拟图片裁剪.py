# _*_ encoding utf-8 _*_


import cv2, os


scale_factor = ['1', '0.25']
for scale in scale_factor:
    dir = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\geometry scaling les\\les-' + scale
    print(dir + ' is on processing')
    for tiffs in os.listdir(dir):
        dir_tiff = dir + '\\' + tiffs
        print(dir_tiff)
        image = cv2.imread(dir_tiff)
        size = image.shape[0:3]
        image_cut = image[106:316, 300:600]
        dir_cut = dir + '-cut\\'
        cv2.imwrite(dir_cut + tiffs, image_cut)
        cv2.destroyAllWindows()
        videoWriter = cv2.VideoWriter(dir_cut + scale + '.avi', cv2.VideoWriter_fourcc(*'mp4v'), 100, (300,210))
    dir_new = dir + '-cut\\'
    for tif_cut in os.listdir(dir_new):
        print(dir_new + tif_cut)
        img_cut = cv2.imread(dir_new + tif_cut)
        videoWriter.write(img_cut)
    input("all done")