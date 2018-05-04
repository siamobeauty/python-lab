import sys
def sum_lines():
    for line in sys.stdin:
        line = line.strip()
        print(line)
        tokens = line.split()
        #print(tokens)
        #print(len(tokens))
        #total = sum([float(token) for token in tokens])
        #上面那行和下面回圈效果是一樣的
#tokens是陣列
        total = 0 
        for i in range(0, len(tokens)):
            total += float(tokens[i])
        print(total)

sum_lines()
