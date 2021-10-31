# 메모리: 29980KB, 시간: 108ms
import sys
input = sys.stdin.readline

n = int(input())
n_list = []
for i in range(n):
    num = int(input())

    if num != 0:
        n_list.append(num)

    else:
        n_list.pop()

print(sum(n_list))
