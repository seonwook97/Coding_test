import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
max = 0
for i in range(n):
    sum_row = 0
    sum_col = 0

    for j in range(n):
        sum_row += map[i][j]
        sum_col += map[j][i]

    if sum_row > max:
        max = sum_row
    
    if sum_col > max:
        max = sum_col

sum_diag = 0
for i in range(n):   
    sum_diag += map[i][i]
    if sum_diag > max:
        max = sum_diag

sum_diag = 0
for i in range(n):
    sum_diag += map[i][n-i-1]
    if sum_diag > max:
        max = sum_diag

print(max)

# end = time.time()
# print(f"{end - start:.5f} sec")