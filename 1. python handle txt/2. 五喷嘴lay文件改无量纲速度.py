import os


distance_folder = ['48', '60', '72']
nozzles_folder = ['5nozzle', '3nozzle', '1nozzle']
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
new_velocity = [40.17478098,36.15730288,32.13982479,28.12234669,24.10486859,18.07865144,16.06991239,14.06117334,12.05243429,10.04369525]
old_velocity = [54.63770214,49.17393192,43.71016171,38.2463915,32.78262128,24.58696596,21.85508085,19.12319575,16.39131064,13.65942553]
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
            # 把无量纲速度和缩放因子关联起来
            file_names = os.listdir(dir_scale)
            velocity_txt = dir_scale + '\\velocity.txt'
            txt_replace = str(old_velocity[num])
            txt_new = str(new_velocity[num])
            lay = open(velocity_txt, "r", encoding="utf-8")
            file_data = ""
            for line in lay:
                line = line.replace(txt_replace, txt_new)
                file_data += line
            lay.close()
            lay_modified = open(velocity_txt, "w", encoding="utf-8")
            lay_modified.write(file_data)
            lay_modified.close()
input("all done")