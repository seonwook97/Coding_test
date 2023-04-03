import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])

    else:
        stack.pop()
        if s[i-1] == '(':           
            cnt += len(stack)

        else:
            cnt += 1 

print(cnt)

# end = time.time()
# print(f"{end - start:.5f} sec")