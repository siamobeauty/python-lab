import sys
#sys是一個模組

def readLines():
    for line in sys.stdin:
        line = line.strip()
        num int(line)
        print(num + 1)


readLines