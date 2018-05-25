#請讀取輸入並建立一個 dictionary, 用來儲存學校的名稱和人數.
#請用迴圈將學校和人數一行一行印出
students = {}

def test():
    num = int(input())
    #print(num)
    for i in range(0, num):
        line = input()
        tokens = line.split()
        print(tokens)
        #students["NCTU-1"] = 2000
        students[tokens[0]+"-1"] = int(tokens[1])
        students[tokens[0]+"-2"] = int(tokens[2])
        students[tokens[0]+"-3"] = int(tokens[3])
        students[tokens[0]+"-4"] = int(tokens[4])
    #print(students)
    num = int(input())
    #print(num)
    for i in range(0, num):
        line = input() 
        print(line, students[line])
        

test()

