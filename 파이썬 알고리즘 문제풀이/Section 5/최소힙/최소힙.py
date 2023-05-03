import math
import time
import sys
import heapq as hq
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
a=[]
while True:
    n = int(input())
    if n == -1:
        break

    if n == 0:
        if len(a) == 0:
            print(-1)

        else:
            print(hq.heappop(a))

    else:
        hq.heappush(a, n)

# end = time.time()
# print(f"{end - start:.5f} sec")