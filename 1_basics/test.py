print("Hello World")
print(9 // 2)
print(9 % 5)
print(3 * 4)


a = 1
b = 2 
print(a + b)


str1 = "I am learning programming."
print(str1)
print(len(str1))

print(str1[2])
print(str1[5:13])
print(str1[5:])
print(str1[:13])
print(str1[:])
print(str1[5:12])
# :13是指在13前的那一個位置


print("{0} {1}".format(100, 200))
print("num1: {0} num2:{1}".format(a, b))
print("{0:10}{1:10}".format(200, 300))
print("{0:<7}{1:<7}{2:<7}"format(12345, 456, 9998))
#<是往左對齊，7是7個字元

s = "stone campus"
# 這個字串的長度
print(len(s))
# 位置6的字母（使用[]）
print(s[6])
# 從位置3到9的子字串"ne Camp"
print(s[3:10])
# 從位置3到最後的子字串"ne Camp"
print(s[3:])