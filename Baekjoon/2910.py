# 메모리: 29200KB, 시간: 76ms
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
num_list = list(map(int, input().split()))
num_set = []
for i in range(n):
    if num_list[i] in num_set:
        continue
    else:
        num_set.append(num_list[i])

count_list = []
for num in num_set:
    count = 0
    for i in range(n):
        if num_list[i] == num:
            count += 1
        else:
            continue
    count_list.append(count)

num_freq = {}
for i in range(len(num_set)):
    num_freq[num_set[i]] = count_list[i]

num_freq = sorted(num_freq.items(), key=lambda x: x[1], reverse=True)

for i in range(len(num_freq)):
    for j in range(num_freq[i][1]):
        print(str(num_freq[i][0]), end=' ')



