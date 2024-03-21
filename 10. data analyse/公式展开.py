import sympy
import numpy as np


x = sympy.Symbol('x')
y = sympy.Symbol('y')
z = sympy.Symbol('z')


ix = [-764.9649, -666.1855, -567.406]


i = 0
while i < 3:
    expr = x**2 + y**2 - 0.847041987*(x-ix[i])**2
    print(expr.expand())
    i+=1

print('all done')