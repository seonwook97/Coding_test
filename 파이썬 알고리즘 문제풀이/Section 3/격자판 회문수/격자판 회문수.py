import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(3): # 열
    for j in range(7): # 행
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1

        for k in range(2):
            if board[i+k][j] != board[i+5-(k+1)][j]:
                break
        
        else:
            cnt += 1

print(cnt)

# end = time.time()
# print(f"{end - start:.5f} sec")