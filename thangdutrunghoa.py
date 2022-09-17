# x=a1(modm1)
# x=a2(modm2)
# x=a3(modm3)
import math
import numpy as np
a = [2, 3, 5]
m = [3, 5, 7]

M = math.prod(m)
M_lst = []
for i in range(len(a)):
    M_lst.append(M//m[i])
y_lst = []
for i in range(len(a)):
    y_lst.append(pow(M_lst[i], -1, m[i]))

a = np.array(a)
M_lst = np.array(M_lst)
y_lst = np.array(y_lst)
x = np.sum(a*M_lst*y_lst) % M
print(x)
