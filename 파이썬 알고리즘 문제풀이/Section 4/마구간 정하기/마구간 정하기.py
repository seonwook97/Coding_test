import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
def count(len):
    cnt = 1
    end_pnt = horizon[0]
    for i in range(1, n):
        if horizon[i] - end_pnt >= len:
            cnt += 1
            end_pnt = horizon[i]
    
    return cnt

n, c = map(int, input().split())
horizon = [int(input()) for _ in range(n)]
horizon.sort()
left = 1
right = horizon[-1]
while left <= right:
    mid = (left + right) // 2
    if count(mid) >= c:
        result = mid
        left = mid + 1
    
    else:
        right = mid - 1

print(result)

# end = time.time()
# print(f"{end - start:.5f} sec")