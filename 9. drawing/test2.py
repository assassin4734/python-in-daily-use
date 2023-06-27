import numpy as np
import statsmodels.api as sm

# generate some random data
X = np.random.rand(100, 3)
y = X[:, 0] + 2*X[:, 1] + 3*X[:, 2] + np.random.randn(100)

# add a constant column to X
X = sm.add_constant(X)

# fit an OLS model
model = sm.OLS(y, X).fit()

# print the summary of the model
print(model.summary())
