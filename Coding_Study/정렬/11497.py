import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    L_list = sorted(list(map(int, input().split())))
    max_value = 0
    for i in range(len(L_list) - 2):
        max_value = max(max_value, L_list[i + 2] - L_list[i])
    print(max_value)

