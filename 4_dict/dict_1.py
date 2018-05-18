ages = {}
def prAge(name):
    if ages.get(name):
        print(name, ages.get(name))
    else:
        print("N/A")

def test():
    #input()的意思是吃到換行，所以在input1裡面吃到3，放進去num裡面
    num = int(input())
    #連吃三行，從0吃到第一個迴圈是
    for i in range(0, num):
        #開始吃Bob 10
        line = input()
        #tokens得到的是一個被切割的list，在切東西的時候習慣用tokens
        tokens = line.split()
        #名字放在0
        name = tokens[0]
        #歲數放在1
        age = int(tokens[1])
        ages[name] = age 
    print(ages)
    #print name and age
    num = int(input())
    for i in range(0, num):
        line = input()
        prAge(line)
test()