import numpy as np

def test():
    arr = [
       [[1, 2, 3],
       [4, 5, 6]]
    ]
    print(arr)
    nparr = np.array(arr)
    print(nparr.ndim)
    print(nparr.shape)
#陣列裡每個數字都乘以2
    print(nparr * 2)

def table(m , n):
    arr = []
    for i in range(0, m):
        sub = []
        for j in range(1, n+1):
            sub.append(i*j)
        arr.append(sub)
    return np.array(arr)
def table1(m, n):
    arr = [i*j for j in range(1, n+1)] for i in range(1, m+1)]
    return np.array(arr)

def test2();
    nparr = table(4, 5)
    print(nparr)
    print(nparr.ndim)
    print(nparr.shape)

test2()

