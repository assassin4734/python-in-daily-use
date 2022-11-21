import os


eq_folder = ["eq=0.55"]
scale_factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
dir = r'F:\eq\postprocessing'
for eq in eq_folder:
    dir_eq = dir + "\\" + eq
    for scale in scale_factor:
        dir_scale = dir_eq + "\\" + str(scale)
        dir_scale_new = dir_eq + "\\40.5-" + str(scale)
        os.rename(dir_scale, dir_scale_new)