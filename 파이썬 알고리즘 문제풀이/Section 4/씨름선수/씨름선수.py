import math
import time
import sys
sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
start = time.time()

# code
n = int(input())
apply_list = [list(map(int, input().split())) for _ in range(n)]
apply_list.sort(key=lambda x:(-x[1], -x[0]))
stack = []
stack.append(apply_list[0])
for i in range(1, n):
    if stack[-1][0] >= apply_list[i][0] and stack[-1][1] >= apply_list[i][1]:
        continue
    else:
        stack.append(apply_list[i]) 

print(len(stack))
end = time.time()
print(f"{end - start:.7f} sec")
# fst_code : 0.0009186 sec