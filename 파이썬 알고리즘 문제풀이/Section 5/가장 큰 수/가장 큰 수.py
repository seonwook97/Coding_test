# 스택
import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m] # 끝에 m자리가 남을 때까지 제거가 안되었다면 뒤에 m만큼 삭제

print(''.join(map(str, stack)))

# end = time.time()
# print(f"{end - start:.5f} sec")