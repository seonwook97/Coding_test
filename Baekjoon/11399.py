# 메모리: 29200KB, 시간: 76ms

import sys
input = sys.stdin.readline

n = int(input())
p_list = sorted(list(map(int, input().split())))
total = 0

for i in range(len(p_list)):
    total += n * p_list[i]
    n -= 1

print(total)






