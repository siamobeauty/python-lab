#list comprehensions
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
  squares.append(x * 2)
print("Example 1",squares)

nums = [0, 1, 2, 3, 4]
#[(x ** 2 ) for x in nums]
#取出來乘以二再放進squares裡面
squares = [x ** 2 for x in nums]
print("Example 2",squares)

nums = [-2, -1, 0, 1, 2]
#
ds = [abs(x) for x in nums if abs(x) < 2]
print("Example 3",ds)

from math import pi
print(pi)
#意思是取到小數點後第三位
print(round(pi, 3))
print("Example 4",[str(round(pi, i))for i in range(1,6)])
