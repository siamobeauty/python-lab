#dictionary的用法
#想要有一個東西來記錄班上的學生的姓名以及對應的歲數，把東西放進去ages裡
#括號中間的值叫key
ages = {}
ages['bob'] = 9
ages['alice'] = 18

#dictionary裡的值
ages['bob']
print(ages['bob'])
print(ages.get('bob'))

#找有沒有john這個值
print(ages.get('john'))
print(ages.get('john', 'N/A' ))

#dictionary的基本寫法
print(len(ages))
print(list(ages))
print('bob' in ages)
print('john' in ages)



