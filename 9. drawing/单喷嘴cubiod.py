import matplotlib
import itertools
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

# 定义matplotlib使用的后台
matplotlib.use('TKAgg')
plt.rcParams['font.sans-serif']=['SimHei']
#定义三个坐标轴
swirl_folder = {'SW-1':0.1, 'SW-2':0.2, 'SW-3':0.3, 'SW-4':0.4, 'SW-5':0.5}
ER_folder = {'ER-1':0.1, 'ER-2':0.2, 'ER-3':0.3, 'ER-4':0.4, 'ER-5':0.5}
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
# 生成散点坐标数据
x_array = np.array([swirl_folder['SW-1'], swirl_folder['SW-2'], swirl_folder['SW-3'], swirl_folder['SW-4'], swirl_folder['SW-5']])
y_array = np.array([ER_folder['ER-1'], ER_folder['ER-2'], ER_folder['ER-3'], ER_folder['ER-4'], ER_folder['ER-5']])
z_array = np.array(scale_factor)
coordinates_swirl= pd.DataFrame(set(list(itertools.product(y_array, z_array))))
coordinates_swirl.insert(0, '0', 0.3)
coordinates_er= pd.DataFrame(set(list(itertools.product(x_array, z_array))))
coordinates_er.insert(1, '0', 0.3)
coordinates_swirl.columns = [0, 1, 2]
coordinates_er.columns = coordinates_swirl.columns
print(coordinates_swirl)
print(coordinates_er)
coordinates = pd.concat([coordinates_swirl, coordinates_er], axis=0)
print(coordinates)
coordinates.to_csv('single swirler coordinates', sep=' ', index=False, header=None)