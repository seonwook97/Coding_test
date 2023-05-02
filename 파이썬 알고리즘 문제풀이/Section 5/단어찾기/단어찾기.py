import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1

for i in range(n - 1):
    word = input()
    p[word] = 0
    
for key, val in p.items():
    if val == 1:
        print(key)
        break

# end = time.time()
# print(f"{end - start:.5f} sec")