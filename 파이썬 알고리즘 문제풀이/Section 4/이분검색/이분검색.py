import math
import time
import sys
import bisect
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

print(bisect.bisect(num_list, m))

# 이분탐색
# left = 0
# right = n - 1
# while left <= right:
#     mid = (left + right) // 2
#     if num_list[mid] == m:
#         print(mid + 1) 
#         break

#     elif num_list[mid] > m:
#         right = mid - 1
    
#     else:
#         left = mid + 1

# end = time.time()
# print(f"{end - start:.5f} sec")