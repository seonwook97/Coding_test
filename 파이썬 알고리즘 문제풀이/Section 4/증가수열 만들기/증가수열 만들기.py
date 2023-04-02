import math
import time
import sys
from collections import deque
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
n = int(input())
num_list = list(map(int, input().split()))
move_res = ''
tmp_num = 0 
# (1) 조건 탐색
# num_list = deque(num_list)
# while num_list:
#     if not num_list:
#         break

#     if tmp_num > max(num_list[0], num_list[-1]): # 양쪽 끝이 현재 수보다 작을 경우 
#         break

#     if tmp_num < num_list[0]:
#         if num_list[-1] < tmp_num or num_list[0] < num_list[-1]:
#             tmp_num = num_list[0]
#             num_list.popleft()
#             move_res += 'L'
    
#     if  tmp_num < num_list[-1]:
#         if num_list[0] < tmp_num or num_list[-1] < num_list[0]:
#             tmp_num = num_list[-1]
#             num_list.pop()
#             move_res += 'R'
# (2) 투 포인터 활용
lt = 0; rt = n - 1
tmp_list = []
while lt <= rt:
    if num_list[lt] > tmp_num:
        tmp_list.append((num_list[lt], 'L'))

    if num_list[rt] > tmp_num:
        tmp_list.append((num_list[rt], 'R'))

    tmp_list.sort()

    if not tmp_list:
        break    

    else:
        move_res += tmp_list[0][1]
        tmp_num = tmp_list[0][0]
        if tmp_list[0][1] == 'L':
            lt += 1
        
        else:
            rt -= 1
    
    tmp_list.clear()

print(len(move_res))       
print(move_res)

# end = time.time()
# print(f"{end - start:.5f} sec")




