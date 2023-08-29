import pandas as pd


dir = "E:\\0-PhD\\1 nozzle\\"
caldata = "对比后的新工况筛选.csv"
dir_caldata = dir + caldata

eq_set = {1:0.03203, 2:0.03786, 3:0.04368, 4:0.0495, 5:0.05532}
swirl_set = {1:'28.5', 2:'35.5', 3:'40.5'}
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]
swirl_folder = ["28.5", "35.5", "40.5", "45.5", "52.5"]


caldata_df = pd.read_csv(filepath_or_buffer=dir_caldata)
print(caldata_df)
