import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i,j))
        if graph[i][j] == 2:
            chicken.append((i,j))

# 치킨집을 어떻게 고를지 조합을 써서 pick_chicken에 담아둔다
pick_chicken = list(combinations(chicken,m))

ans = []
for i in pick_chicken: # 조합해놓은 치킨집 좌표 를 돌리면서
    total = 0
    for j in house: # 저장해놓은 집의 좌표를 돌리면서
        Min = 10001
        for k in i: # 치킨집 좌표랑 집의 좌표를 빼주는데 여기서 최솟값을 찾는다
            dist = abs(k[0]-j[0])+abs(k[1]-j[1])
            Min = min(Min,dist)
        total += Min
    ans.append(total)
print(min(ans))