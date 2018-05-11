def prList(arr):
    #index is last one, then println. otherwise, ","
    #x代表位置，y代表數值
    for x,y in enumerate(arr):
        if(x!=len(arr)-1):
            print(y,end=",")
        else:
            print(y)
a = [10,20,30,40,50]
b = [30,4,56]
prList(a)
prList(b)

''' Problem. 2
'''
def enumList(arr):
    # 1. apple
    for idx,el in enumerate(arr):
       # print(idx+1, el)
       print("{}. {}".format(idx+1,el) )
enumList(['apple', 'orange', 'banana'])

