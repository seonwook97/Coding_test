import math
import time
import sys
from collections import deque
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
n, m = map(int, input().split())
weight_list = list(map(int, input().split()))
weight_list.sort()
weight_list = deque(weight_list)
cnt = 0
while weight_list:
    if len(weight_list) == 1: # 자료형 안에 값이 한개가 남았을 때 return
        cnt += 1
        break

    if weight_list[0] + weight_list[-1] > m: 
        weight_list.pop() # 가장 무거운 사람 1명 out
        cnt += 1
    
    else:
        weight_list.popleft() # 가벼운 사람 out
        weight_list.pop() # 무거운 사람 out
        cnt += 1
    
print(cnt)

# end = time.time()
# print(f"{end - start:.5f} sec")
# using list : 0.00101 sec
# using deque : 0.00091 sec
