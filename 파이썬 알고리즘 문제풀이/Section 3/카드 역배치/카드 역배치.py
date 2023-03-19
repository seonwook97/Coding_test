import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
change_order = [list(map(int, input().split())) for i in range(10)]
num_list = [i for i in range(21)]
for a, b in change_order:
    for i in range((b - a + 1) // 2): 
        num_list[a + i], num_list[b - i] = num_list[b - i], num_list[a + i]

num_list.pop(0)
print(' '.join(map(str, num_list)))

# end = time.time()
# print(f"{end - start:.5f} sec")