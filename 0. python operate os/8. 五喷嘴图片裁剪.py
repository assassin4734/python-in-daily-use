# _*_ encoding utf-8 _*_


import cv2


distance_folder = ['48', '60', '72']
nozzles_folder = ['5nozzle', '3nozzle', '1nozzle']
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
quantities = ['velocity.tiff', 'ch+.tiff', 'flame.tiff']
for nozzles in nozzles_folder:
    # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle
    dir_nozzles = 'E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\postprocessing\\' + nozzles
    print(dir_nozzles + ' is on processing')
    for distance in distance_folder:
        # E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48
        dir_distance = dir_nozzles + '\\' + distance
        for num in range(len(scale_factor)):
            str_factors = str(scale_factor[num]) 
            #  E:\\0-PhD\\5 nozzle\\5nozzle-DLN2.6SIZE\\5nozzle\\48\\48-1
            dir_scale = dir_distance + '\\' + distance + '-' + str_factors
            for quantity in quantities:
                dir_phs = dir_scale + '\\' + quantity
                print(dir_phs + ' is on going')
                image_cut = cv2.imread(dir_phs)
                size = image_cut.shape[0:3]
                print(size)
                if quantity == 'velocity.tiff':
                    image_cut = image_cut[0:939, 65:1642]
                else:
                    image_cut = image_cut[0:939, 65:930]
                cv2.imwrite(dir_phs.replace(".tiff", "-cut.tiff"), image_cut)
                cv2.destroyAllWindows()
input("all done")