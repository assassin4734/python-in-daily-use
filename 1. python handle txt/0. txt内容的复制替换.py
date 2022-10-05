# _*_ encoding utf-8 _*_


# 定义目录以及处理数据的列表
distance_folder = ['48', '60', '72']
nozzles_folder = ['5nozzle', '3nozzle', '1nozzle']
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
d = 0.096
velocity = [54.63770214, 49.17393192, 43.71016171, 38.2463915, 32.78262128, 24.58696596, 
            21.85508085, 19.12319575, 16.39131064, 13.65942553]
quantities = ['velocity', 'ch+', 'flame']
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
            # 定义替换变量
            scale_val = str(d*scale_factor[num])
            velocity_val = str(velocity[num])
            new_text_v28 = "V2/" + scale_val
            new_text_v29 = "V3/" + scale_val
            new_text_v30 = "V19/" + velocity_val
            new_text_v31 = "V16/" + velocity_val
            # 开始替换
            for quantity in quantities:
                dir_quantity = dir_scale + '\\' + quantity + '.txt'
                file_data = ""
                lay = open(dir_quantity, "r", encoding="utf-8")
                for line in lay:
                    line = line.replace("V2/0.096", new_text_v28)
                    line = line.replace("V3/0.096", new_text_v29)
                    line = line.replace("V19/54.63770214", new_text_v30)
                    line = line.replace("V16/54.63770214", new_text_v31)
                    file_data += line
                lay.close()
                lay_modified = open(dir_quantity, "w", encoding="utf-8")
                lay_modified.write(file_data)
                lay_modified.close()
input("all done")