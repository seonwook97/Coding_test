import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
l = int(input())
height_list = list(map(int, input().split()))
m = int(input()) 
height_list.sort(reverse=True)
for _ in range(m):
    height_list[0] -= 1 
    height_list[-1] += 1
    height_list.sort(reverse=True)

print(height_list[0] - height_list[-1])
# end = time.time()
# print(f"{end - start:.5f} sec")