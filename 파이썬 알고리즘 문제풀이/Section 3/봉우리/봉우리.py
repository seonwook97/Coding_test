import math
import time
import sys
from collections import deque
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
n = int(input())
map = deque(list(map(int, input().split())) for _ in range(n))
map.appendleft([0] * n)
map.append([0] * n)
for row in map: # 격자 채우기
    row.insert(0, 0)
    row.append(0)

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        # (1) 모든 방향보다 클 때
        # if all(map[i][j] > map[i+dx[k]][j+dy[k]] for k in range(4)):
        #     cnt += 1
        
        # (2) 최대값 이용
        max_num = max(map[i][j-1], map[i][j+1], map[i-1][j], map[i+1][j])
        if map[i][j] > max_num:
            cnt += 1

print(cnt)

# end = time.time()
# print(f"{end - start:.5f} sec")