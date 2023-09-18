import numpy as np
import pandas as pd
import matplotlib


matplotlib.use('TKAgg')


a1 = np.array([[80, 100, 40],[100, 170, 140],[40, 140, 200]])
A = pd.DataFrame(a1)
print(A)
lsm, svm, rsm = np.linalg.svd(A)
print(pd.DataFrame(lsm))
print(pd.DataFrame(svm))
print(pd.DataFrame(rsm))
a2 = lsm.dot(rsm)
print(pd.DataFrame(a2))
svm = pd.DataFrame(np.array([[360, 0, 0],[0, 90, 0],[0, 0, 0]]))
print(svm)
a3 = lsm.dot(svm)
print((pd.DataFrame(a3)))
a4 = a3.dot(rsm)
print((pd.DataFrame(a4)))