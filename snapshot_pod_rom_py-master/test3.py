import numpy as np
from sklearn.linear_model import LinearRegression

# generate some random data
X = np.random.rand(100, 3)
y = X[:, 0] + 2*X[:, 1] + 3*X[:, 2] + np.random.randn(100)

# fit a linear regression model
model = LinearRegression().fit(X, y)

# print the current coefficients
print("Current coefficients:", model.coef_)

# define a list of new coefficients
new_coefs = [1, 2, 3]

# set the new coefficients in the model
model.coef_ = np.array(new_coefs)

# print the new coefficients
print("New coefficients:", model.coef_)
