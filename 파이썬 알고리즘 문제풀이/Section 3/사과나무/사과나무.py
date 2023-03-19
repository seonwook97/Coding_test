import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
sum = 0
left = right = n // 2 # 중앙
for i in range(n):
    for j in range(left, right + 1):
        sum += map[i][j]
    
    if i < n // 2: # 중앙 전
        left -= 1
        right += 1
    
    else: # 중앙 후
        left += 1
        right -= 1

print(sum)

# end = time.time()
# print(f"{end - start:.5f} sec")