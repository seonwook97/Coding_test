import sys
# sys.stdin = open('in1.txt', 'rt')
n, m = map(int, input().split())
count_list = [0] * (n + m + 1)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        count_list[i + j] += 1 # 주사위의 합을 index, 나오는 횟수를 value

for i in range(n + m + 1):
    if count_list[i] == max(count_list): # 가장 많이 나온 주사위 합(idx) 반환
        print(i, end=' ')






