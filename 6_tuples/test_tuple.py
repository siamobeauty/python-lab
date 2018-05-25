#arr = [100, 200, 300]

book1 = ("#010", "Stone Programming", 330)
(id1, title1, price1)= book1

book2 = "#025", "Python Programming", 230
id2, totle2, price2 = book2 

print(book1)
print(book1[0], book1[1], book1[2])
print(id1, title1, price1)

arr = [100, 200, 300]
#enumerate回傳的是一個tuple值，才可以同時得到idx和裡面的val
for (idx, val) in enumerate(arr):
    print(idx, val)