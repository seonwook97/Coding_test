import sys
input = sys.stdin.readline
n, m = map(int, input().split())
w_lst = [0] + list(map(int, input().split()))
comb = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    comb[a].append(b)
    comb[b].append(a)

cnt = 0
for i in range(1, n+1):
    flag = True
    for f in comb[i]:
        if w_lst[i] <= w_lst[f]:
            flag = False
            break
    
    if flag == True:
        cnt += 1

print(cnt)