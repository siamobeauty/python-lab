import numpy as np

#產生3*4的0矩陣，裡面都是0
mat1 = np.zeros((3, 4))
#print(mat1)
#print(mat1.ndim)
#print(mat1.shape)

#產生3*3的1矩陣，裡面都是1
mat2 = np.ones((3, 3)) * 2
mat2_2 = mat2 * 2 
#mat2 * mat2_2每個數相乘
mat2_3 = mat2 * mat2_2
#2*4+2*4+2*4，矩陣相乘
mat2_4 = np.matmul(mat2, mat2_2)
print(mat2)
print(mat2_2)
print(mat2_3)
print(mat2_4)

mat3 = np.eye(3)
#print(2)
#print(3)
#print(mat2 * mat3)
#print(np.matmul(mat2, mat3))

import matplotlib.pyplot as plt

arr_x = np.arange(10)
#a產生一個0-1的數字（不等於1)，長度為10的矩陣
a = np.random.rand(10)
#b在5-9裡面產生一個長度為10的矩陣
b = np.random.randint(5, 10, 10)
#print(arr_x)
#print(a)
#print(b)
#plt.plot(arr_x, a, '-r^', arr_x, b, '--go')
#plt.show()
