import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
def DFS(x):
    if x == 0:
        return
    
    else:
        DFS(x // 2)
        print(x % 2, end='')

n = int(input())
DFS(n)

# end = time.time()
# print(f"{end - start:.5f} sec")