# 숫자 게임
def solution(A, B):
    A.sort() 
    B.sort()
    result = 0
    for i in A:
        for j in B:
            if j > i:
                B.remove(j)
                result += 1
                break
    
    return result