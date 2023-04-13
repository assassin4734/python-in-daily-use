from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Generate some sample data
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([5, 12, 21])

# Create polynomial features of degree 4
poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)

# Train a linear regression model on the polynomial features
model = LinearRegression()
model.fit(X_poly, y)

# Print out the features and coefficients
features = model.get_feature_names()
for i in range(len(features)):
    print(features[i], model.coef_[i])
    print('\n')
    # print(len(features))
model.coef_[0] = 100
for i in range(len(features)):
    print(features[i], model.coef_[i])
    # print(len(features))
