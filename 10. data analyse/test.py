from sklearn import preprocessing
X = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]
X = preprocessing.scale(X, with_mean=False)
print(X)
Y = [1, 0.95, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35]
Y = preprocessing.scale(Y, with_mean=False)
print(Y)