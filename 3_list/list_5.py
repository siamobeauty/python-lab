
#Q1:squareList(nums): 回傳一個 list, 其中的元素為 nums 中每個數字的平方, 例如: squareList([3, 4, 5]) 回傳 [9, 16, 25]
#Q2:absList(nums, x): 回傳一個 list, 其中的元素為 nums 中絕對值小於 x 的數字, 例如: absList([3, 4, -1, -2, 2, 7, 1], 3) 回傳 [-1, -2, 2, 1]
#Q3:piList(n): 回傳一個 list, 其中的元素為從小數第 1 位到第 n 位的 pi 值, 例如 : piList(5) 回傳 [3.1, 3.14, 3.142, 3.1416, 3.14159]

#下面要用到pi，所以先import
from math import pi
def squareList(nums):
    return [x**2 for x in nums]
def absList(nums, x):
    return [x for x in nums if abs(x)<3]
def piList(n):
    return [round(pi,i) for i in range(1,n+1)]


print("Q1",squareList([3, 4, 5]))
print("Q2",absList([3, 4, -1, -2, 2, 7, 1], 3))
print("Q3",piList(5))
