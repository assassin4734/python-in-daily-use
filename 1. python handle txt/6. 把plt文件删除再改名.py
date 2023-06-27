import os
import re


dir = 'E:\\0-PhD\\1 nozzle\\add-pod\\'
folder = ["z-28.5", "z-35.5", "z-52.5"]
folder = ["z-40.5"]
scale_factor = [0.95, 0.85, 0.75, 0.65, 0.55, 0.45, 0.35]
# scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]
exa = '28.5-1.plt'
for folders in folder: 
    dir_folder = dir + folders + '\\'
    for scale in scale_factor:
        dir_scale = dir_folder + str(scale) + '\\'
        try:
            os.remove(dir_scale + exa)
        except:
            pass
        file_names = os.listdir(dir_scale)
        for names in file_names:
            if re.search(".plt", names, re.I):
                os.rename(dir_scale + names, dir_scale + exa)