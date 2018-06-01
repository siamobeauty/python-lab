import numpy as np
import matplotlib.pyplot as plt

arr = np.arange(10)
#[0 1 2 3 4 5 6 7 8 9]
print(arr)
#ndim陣列只有一層
print(arr.ndim)
#shape陣列裡面第一層的長度
print(arr.shape)

#從5開始到20，間隔是2 
arr2_x = np.arange(5, 20, 2)
arr2_y = arr2_x ** 1.2 + 1
print(arr2_x)
print(arr2_y)

arr3_x = np.arange(10, 50, 3)
arr3_y = arr3_x * 2 + 5

arr4_x = np.linspace(0, 10, 21)
arr4_y1 = arr4_x * 2
arr4_y2 = arr4_x * 3
print(arr4_x)


# 線的格式＝---. b=blue, o是要用原點
plt.plot(arr4_x, arr4_y1, '-rv', arr2_x, arr2_y, '-rv', arr3_x, arr3_y, '--bo')
plt.show()