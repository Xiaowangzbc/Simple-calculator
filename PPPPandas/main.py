import numpy as np
#一维数组
a1 = np.array([1,2,3,4,5,])
print(a1)
#二维数组
a2 = np.array([[1,2],[3,4],[5,6]])
print(a2)
#全0数组
a3 = np.zeros((3,4))
print(a3)
a4 = np.ones((2,3))
print(a4)

a5 = np.eye(3)
print(f'这是单位矩阵:\n{a5}')
a6 = np.arange(0,10,2)
print(f'这是等差数组:\n{a6}')
a6 = np.linspace(0,1,5)
print(f'这是等间距数组\n{a6}')
