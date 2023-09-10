import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
def DFS(L, sum):
    global res
    if L >= res:
        return
    
    if sum > m:
        return
    
    if sum == m:
        if L < res:
            res = L

    else:
        for i in range(n):
            DFS(L + 1, sum + a[i])

if __name__=="__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    res = 2147000000
    a.sort(reverse=True)
    DFS(0, 0)
    print(res)

# end = time.time()
# print(f"{end - start:.5f} sec")