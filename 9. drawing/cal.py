import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd
# a = b0 + b1*b + b2*c + b3*d + b4*b^2 + b5*c^2 + b6*d^2 + b7*b*c + 
# b8*b*d + b9*c*d + b10*b^3 + b11*c^3 + b12*d^3 + b13*b^2*c + b14*b^2*d + 
# b15*b*c^2 + b16*b*d^2 + b17*c^2*d + b18*c*d^2 + b19*b*c*d
# create dataset
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
c = np.array([3, 4, 5, 6])
d = np.array([4, 5, 6, 7])
# organize data into input and target arrays
X = np.column_stack((b, c, d))
y = a
# create PolynomialFeatures object with degree 3
poly = PolynomialFeatures(degree=3)
# transform the input data
X_poly = poly.fit_transform(X)
model = LinearRegression()
p = model.fit(X_poly, y)
print(p)
new_b = np.array([2, 3, 4, 5])
new_c = np.array([3, 4, 5, 6])
new_d = np.array([4, 5, 6, 7])

new_X = np.column_stack((new_b, new_c, new_d))
new_X_poly = poly.transform(new_X)
predicted_a = model.predict(new_X_poly)
r2 = r2_score(y_true=a, y_pred=predicted_a)
print(r2)
print(predicted_a)
print(model.coef_)
