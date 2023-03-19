# 투 포인터
import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
n, m = map(int, input().split())
a = list(map(int, input().split()))
left = 0
right = 1
sum = a[0]
cnt = 0
while True:
    if sum < m:
        if right < n:
            sum += a[right]
            right += 1
        else:
            break
    
    elif sum == m:
        cnt += 1
        sum -= a[left]
        left += 1
    
    else:
        sum -= a[left]
        left += 1

print(cnt)          

# end = time.time()
# print(f"{end - start:.5f} sec")