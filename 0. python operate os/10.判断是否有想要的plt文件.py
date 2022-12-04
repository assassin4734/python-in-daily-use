import os

eq_folder = ["eq=0.55", "eq=0.65", "eq=0.75", "eq=0.85", "eq=0.95"]
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
posi = []
for eq in eq_folder:
    dir_post = 'E:\\0-PhD\\1 nozzle\eq\\postprocessing\\' + eq
    for num in range(len(scale_factor)):
        factors = scale_factor[num]
        str_factors = str(factors) 
        # plt的保存路径
        tecplot_place = dir_post + '\\40.5-' + str_factors + '\\28.5-1-V'
        if os.path.lexists(tecplot_place + ".plt") == False:
            posi.append(tecplot_place)
for element in posi:
    print(element)
input("done")