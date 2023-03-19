import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
fst_num = int(input())
fst_list = list(map(int, input().split()))
scd_num = int(input())
scd_list = list(map(int, input().split()))

new_list = []
for i in range(fst_num):
    new_list.append(fst_list[i])

for i in range(scd_num):
    new_list.append(scd_list[i])

print(' '.join(map(str, sorted(new_list))))

# end = time.time()
# print(f"{end - start:.5f} sec")