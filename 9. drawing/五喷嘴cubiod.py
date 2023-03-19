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
distance_folder = {'48':0.1, '60':0.2, '72':0.3}
nozzles_folder = {'MF':0.1, 'MS':0.2, 'MP':0.3}
scale_factor = [1, 0.9, 0.8, 0.7, 0.6, 0.45, 0.4, 0.35, 0.3, 0.25]
# 生成散点坐标数据
x_array = np.array([distance_folder['48'], distance_folder['60'], distance_folder['72']])
y_array = np.array([nozzles_folder['MF'], nozzles_folder['MS'], nozzles_folder['MP']])
z_array = np.array(scale_factor)
coordinates = pd.DataFrame(set(list(itertools.product(x_array, y_array, z_array))))
print(coordinates)
coordinates.to_csv('coordinates', sep=' ', index=False, header=None)
# 定义图
fig = plt.figure(figsize=(10, 20), dpi=80)
ax = fig.add_subplot(111, projection='3d')
# 画出散点
ax.scatter(coordinates[0], coordinates[1], coordinates[2], s=150, c=np.random.rand(90))
# 画位置
matplotlib.rcParams['lines.linewidth'] = 20
# 设置坐标轴比例
ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([0.5, 0.5, 1, 1]))
# 设置坐标轴始终
ax.set(xlim=[0, 0.4], ylim=[0, 0.4], zlim=[0.25, 1])
# 设置坐标间隔
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
# 调整图的大小和位置
plt.subplots_adjust(top=1.1,bottom=0,left=0,right=1.5,hspace=0,wspace=0)
plt.show()