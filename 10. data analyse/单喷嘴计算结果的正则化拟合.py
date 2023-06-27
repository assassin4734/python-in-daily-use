import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
import pandas as pd


pd.set_option("mode.chained_assignment", None)


# 定义位置和存放数据的excel表
dir = r'E:\0-PhD\1 nozzle'
data_ori = r'\流场特征和火焰特征矩阵.xlsx'
dir_data_ori = dir + data_ori
characteristic = pd.read_excel(io=dir_data_ori, header=0, sheet_name='变量优化')
print(characteristic)
# 定义训练集的坐标变量
print('# 定义坐标变量')
q_c = np.array(characteristic['Q'])
sw_c = np.array(characteristic['SW'])
er_C = np.array(characteristic['ER'])
X = np.column_stack((q_c, sw_c, er_C))
X = preprocessing.scale(X)
print(X)
# 定义检验集的坐标变量
test = pd.read_excel(io=dir_data_ori, header=0, sheet_name='检验')
q_t = np.array(test['Q'])
sw_t = np.array(test['SW'])
er_t = np.array(test['ER'])
X_t = np.column_stack((q_t, sw_t, er_t))
# X_t = preprocessing.scale(X_t)
print('看看检验矩阵的坐标')
print(X_t)
# 把训练数据转化为array然后输出看看
Eye_axial = np.array(characteristic['涡心轴向位置'])
print('涡心轴向位置：\n')
print(Eye_axial)
Eye_radial = np.array(characteristic['涡心径向位置'])
print('涡心径向位置：\n')
print(Eye_axial)
Flame_length = np.array(characteristic['火焰长度'])
print('火焰长度：\n')
print(Flame_length)
Flame_angle = np.array(characteristic['火焰张角'])
print('火焰张角：\n')
print(Flame_angle)
# 把检验数据转化为array然后输出看看
Eye_axial_t = np.array(test['涡心轴向位置'])
print('涡心轴向位置：\n')
print(Eye_axial_t)
Eye_radial_t = np.array(test['涡心径向位置'])
print('涡心径向位置：\n')
print(Eye_axial_t)
Flame_length_t = np.array(test['火焰长度'])
print('火焰长度：\n')
print(Flame_length_t)
Flame_angle_t = np.array(test['火焰张角'])
print('火焰张角：\n')
print(Flame_angle_t)
# 定义特征数据集合
list_var = [Eye_axial, Eye_radial, Flame_length, Flame_angle]
# 定义检验数据集合
list_var_t = [Eye_axial_t, Eye_radial_t, Flame_length_t, Flame_angle_t]
name = ['涡心轴向位置预测', '涡心径向位置预测', '火焰长度预测', '火焰张角预测']
# 定义预测值的集合
list_pre = []
# 定义检验预测值的集合
list_pre_t = []
# 定义拟合优度的集合
r2_fit = []
# 定义检验拟合优度的集合
r2_fit_t = []
# 定义截距的集合
cept_fit=[]
print('# 进行拟合')
n = int(input('输入拟合阶数：'))
for s in range(len(list_var)):
    # 定义训练集的因变量
    Y = list_var[s]
    # 定义检验集的因变量
    Y_t = list_var_t[s]
    # 开始训练
    poly = preprocessing.PolynomialFeatures(degree=n)
    X_poly = poly.fit_transform(X)
    model = Ridge(alpha=1)
    p = model.fit(X_poly, Y)
    # model.intercept_ = 0
    # 使用训练好的函数拟合并预测
    predicted_Y = model.predict(X_poly)
    cept_fit.append(model.intercept_)
    # test
    # test_data = np.array([0.9, 0.42, 0.65]).reshape(1, -1)
    # test_data_poly = poly.transform(test_data)
    # new = model.predict(test_data_poly)
    # test end
    r2 = r2_score(y_true=Y, y_pred=predicted_Y)
    print('# 预测值为：')
    print(predicted_Y)
    print('# 拟合优度为：')
    print(r2)
    r2_fit.append(r2)
    list_pre.append(list(predicted_Y))
    # 保存拟合参数
    print('# 保存拟合参数：')
    co = model.coef_
    print(co)
    print(len(co))
    coeold = pd.DataFrame(np.array(co).reshape(-1))
    coeold.to_excel(dir + '//原本的拟合系数' + name[s] + '.xlsx')
    # 进行检验
    X_t_poly = poly.fit_transform(X_t)
    predicted_Y_test = model.predict(X_t_poly)
    # r2_t = r2_score(y_true=Y_t, y_pred=predicted_Y_test)
    # r2_fit_t.append(r2_t)
    list_pre_t.append(list(predicted_Y_test))

# 定义预测矩阵表
dic_pre = dict(zip(name, list_pre))
data_pre = pd.DataFrame(dic_pre)
# 定义检验的预测矩阵表
dic_pre_t = dict(zip(name, list_pre_t))
data_pre_t = pd.DataFrame(dic_pre_t)
# 定义拟合优度表
dic_r2 = dict(zip(name, r2_fit))
r2_pre = pd.DataFrame(dic_r2, index=[0])
# 定义预测的拟合优度表
dic_r2_t = dict(zip(name, r2_fit_t))
r2_pre_t = pd.DataFrame(dic_r2_t, index=[0])
# 定义截距表
dic_cept = dict(zip(name, cept_fit))
data_cept = pd.DataFrame(dic_cept, index=[0])
# 保存excel表
data_pre.to_excel(dir + r'\预测矩阵.xlsx')
r2_pre.to_excel(dir + r'\拟合优度.xlsx')
data_cept.to_excel(dir + r'\截距.xlsx')
data_pre_t.to_excel(dir + r'\检验值的预测矩阵.xlsx')
r2_pre_t.to_excel(dir + r'\检验值的拟合优度.xlsx')


input("拟合与检验完成")