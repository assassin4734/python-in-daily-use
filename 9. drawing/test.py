from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures  # 用于解决欠拟合的问题的多项式回归
from sklearn.linear_model import Ridge  # 用于处理过拟合的正则化处理
matplotlib.use('TKAgg')
# 自己定义训练数据
x_train = [[6], [8], [10], [14], [18]]  # 大小
y_train = [[7], [9], [13], [17.5], [18]]  # 价格

# 进行阶数为一阶的线性回归和预测
linear = LinearRegression()
linear.fit(x_train, y_train)

# 绘制基于出原始样本数据得出来的拟合曲线 + 散点图
xx = np.linspace(0, 25, 100)
xx = xx.reshape(-1, 1)
yy = linear.predict(xx)
plt.scatter(x_train, y_train)
plt.plot(xx, yy)
plt.show()

"""使用更高次的多项式回归产生一个过拟合的结果"""
# 建立二次多项式线性回归模型进行预测
poly5 = PolynomialFeatures(degree=3)  # 5次多项式特征生成器
x_train_poly5 = poly5.fit_transform(x_train)
# 建立模型预测
linear5_poly5 = LinearRegression()
linear5_poly5.fit(x_train_poly5, y_train)
print('未经过岭回归时的各项特征的权重', linear5_poly5.coef_)

# 绘制基于多项式回归后得出来的拟合曲线 + 散点图
xx_poly5 = poly5.transform(xx)
yy_poly5 = linear5_poly5.predict(xx_poly5)
plt.scatter(x_train, y_train)
plt.plot(xx, yy, label="Degree = 1")
plt.plot(xx, yy_poly5, label="Degree = 5")
plt.legend()
plt.show()

"""使用Ridge岭回归解决出现的过拟合问题"""
# 建立二次多项式线性回归模型进行预测
poly5 = PolynomialFeatures(degree=3)  # 5次多项式特征生成器
x_train_poly5 = poly5.fit_transform(x_train)
# 建立模型预测
linear5_poly5_new = Ridge(alpha=0.8)
linear5_poly5_new.fit(x_train_poly5, y_train)
print('经过岭回归后的各项特征的权重', linear5_poly5.coef_)

# 绘制基于多项式回归后得出来的拟合曲线 + 散点图
xx_poly5 = poly5.transform(xx)
yy_poly5 = linear5_poly5_new.predict(xx_poly5)
plt.scatter(x_train, y_train)
plt.plot(xx, yy, label="Degree = 1")
plt.plot(xx, yy_poly5, label="Degree = 5")
plt.legend()
plt.show()
