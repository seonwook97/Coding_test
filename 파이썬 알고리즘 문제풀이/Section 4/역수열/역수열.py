import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
n = int(input())
num_list = list(map(int, input().split()))
seq = [0] * n
for i in range(n):
    for j in range(n):
        if num_list[i] == 0 and seq[j] == 0:
            seq[j] = i + 1
            # print(j, seq[j])
            break
        
        elif seq[j] == 0:
            num_list[i] -= 1
            # print(num_list[i])

for cnt in seq:
    print(cnt, end=' ')

# end = time.time()
# print(f"{end - start:.5f} sec")