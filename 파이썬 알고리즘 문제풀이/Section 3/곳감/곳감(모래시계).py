# 스택
import math
import time
import sys
from collections import deque
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
n = int(input())
map_list = [deque(list(map(int, input().split()))) for _ in range(n)]
m = int(input())

for _ in range(m):
    row_num, direct, move = map(int, input().split())
    if direct == 0:
        for _ in range(move):
            map_list[row_num-1].rotate(-1) # 젤 빠르지롱 0.00000sec
    
    if direct == 1:
        for _ in range(move):
            map_list[row_num-1].rotate(1)

sum = 0
left, right = 0, n
for i in range(n):
    for j in range(left, right):
        sum += map_list[i][j]
    
    if i < n // 2:
        left += 1
        right -= 1
    
    else:
        left -= 1
        right += 1

print(sum)

# end = time.time()
# print(f"{end - start:.5f} sec")