import numpy as np
import os
from sklearn import preprocessing
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
import pandas as pd


pd.set_option("mode.chained_assignment", None)


def choosing(display_str):
    print("-" * 20)
    print(display_str)
    print("exit退出")
    print("-" * 20)
    action_str = input()
    try:
        if ['0', '1', '2', '3'].count(action_str) == True:
            return int(action_str)
        else:
            print("输入错误，请重新输入")
            choosing(display_str)
    except:
        if action_str == 'exit':
            os._exit(0)
        print("编号输入错误，请重新输入")
        choosing(display_str)


import numpy as np


dir = r'E:\0-PhD\1 nozzle'
data_ori = r'\流场特征和火焰特征矩阵.xlsx'
dir_data_ori = dir + data_ori
characteristic = pd.read_excel(io=dir_data_ori, header=0, sheet_name='变量优化')
print(characteristic)
print('# 定义坐标变量')
q_c = np.array(characteristic['Q'])
sw_c = np.array(characteristic['SW'])
er_C = np.array(characteristic['ER'])
X = np.column_stack((q_c, sw_c, er_C))
X = preprocessing.scale(X)
print(X)
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
list_var = [Eye_axial, Eye_radial, Flame_length, Flame_angle]
name = ['涡心轴向位置预测', '涡心径向位置预测', '火焰长度预测', '火焰张角预测']
list_pre = []
r2_fit = []
cept_fit=[]
print('# 进行拟合')
n = int(input('输入拟合阶数：'))
for s in range(len(list_var)):
    # 定义训练集的因变量
    Y = list_var[s]
    # 开始训练
    poly = preprocessing.PolynomialFeatures(degree=n)
    X_poly = poly.fit_transform(X)
    model = Ridge()
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
    print('# 保存拟合参数：')
    co = model.coef_
    print(co)
    print(len(co))
    coeold = pd.DataFrame(np.array(co).reshape(5, -1))
    coeold.to_excel(dir + '//原本的拟合系数' + name[s] + '.xlsx')
    newcoelist = []
    # for coe in model.coef_:
    #     if abs(coe) < 10**2:
    #         coe = 0
    #     # coe_new = coe/(10**12)
    #     coe_new = coe
    #     newcoelist.append(coe_new)
    # # test
    # newcoelist = np.array(newcoelist)
    # model.coef_ = newcoelist
    # p2 = model.predict(X_poly)
    # test end
    # newcoelist = pd.DataFrame(np.array(newcoelist).reshape(5, -1))
    # print(newcoelist)
    # newcoelist.to_excel(dir + '//拟合系数' + name[s] + '.xlsx')
dic_pre = dict(zip(name, list_pre))
dic_r2 = dict(zip(name, r2_fit))
dic_cept = dict(zip(name, cept_fit))
data_pre = pd.DataFrame(dic_pre)
data_pre.to_excel(dir + r'\预测矩阵.xlsx')
r2_pre = pd.DataFrame(dic_r2, index=[0])
r2_pre.to_excel(dir + r'\拟合优度.xlsx')
data_cept = pd.DataFrame(dic_cept, index=[0])
data_cept.to_excel(dir + r'\截距.xlsx')
print(data_pre)
print(r2_pre)