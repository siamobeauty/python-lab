#現在想進行 4 位數字的 Bulls and Cows 遊戲, 請你寫一個函數 result(answer, guess) 回傳 guess 和 answer 的比較結果.
#例如: result('1234', '4321') 回傳 '0A4B', result('4657', '9658') 回傳 '2A0B', result('9876', '6879') 回傳 '2A2B'
nums1=[1,2,3,4]
nums2=[4,5]
print([])
#way1
def result(answer, guess):
    A=0
    B=0
    for idx_ans, val_ans in enumerate(answer):
        if answer[idx_ans] == guess[idx_ans]:
            A+= 1
        else:
            for idx_gue, val_gue in enumerate(guess):
                if val_ans==val_gue and idx_ans != idx_gue:
                   B+=1
        
    return str(A)+"A"+str(B)+"B"

print(result('1234', '4321'))
print(result('4657', '9658'))
print(result('9876', '6879')) 


#ways2
def result(answer, guess):
    A=0
    B=0
    for idx_ans, val_ans in enumerate(answer):
        if answer[idx_ans] == guess[idx_ans]:
            A+= 1
        elif val_ans in guess:
            B+=1
    return str(A)+"A"+str(B)+"B"
print(result('1234', '4321'))
print(result('4657', '9658'))
print(result('9876', '6879')) 
