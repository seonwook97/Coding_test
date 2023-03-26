import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
def count(len):
    cnt = 0
    for x in line:
        cnt += (x // len)
    
    return cnt

line = []
max_line = 0
k, n = map(int, input().split())
for i in range(k):
    temp=int(input())
    line.append(temp)
    max_line=max(max_line, temp)

left = 1
right = max_line
while left <= right:
    mid = (left + right) // 2
    if count(mid) >= n:
        result = mid
        left = mid + 1

    else:
        right = mid - 1

print(result)

# end = time.time()
# print(f"{end - start:.5f} sec")

# sort_reverse : 0.00099 sec
# max 저장 : 0.00000 sec