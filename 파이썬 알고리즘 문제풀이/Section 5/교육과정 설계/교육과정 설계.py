import math
import time
import sys
from collections import deque
sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i + 1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" %(i + 1))
        else:
            print("#%d NO" %(i + 1))

# end = time.time()
# print(f"{end - start:.5f} sec")