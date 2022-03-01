import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph_list = []
for _ in range(h):
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    graph_list.append(graph)
# print(graph_list[0])
# print(graph_list[1])

dy = [-1, 1, 0, 0, 0, 0] # 2차원 상, 하, 좌, 우
dx = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1] # 3차원 위, 아래
q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph_list[i][j][k] == 1: # 익은 토마토로부터 인접한 토마토들이 익어가기 때문에
                q.append([i, j, k])

def bfs():
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= nz < h and 0 <= ny < n and 0 <= nx < m) and graph_list[nz][ny][nx] == 0:
                graph_list[nz][ny][nx] = graph_list[z][y][x] + 1
                q.append([nz, ny, nx])

bfs()
print(graph_list)

# 예외처리
max_day = 0
flag = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph_list[i][j][k] == 0: # 하나라도 익지 않은 토마토가 있다면
                flag = False

            max_day = max(max_day, graph_list[i][j][k])

if not flag:
    print(-1)

else:
    print(max_day - 1) # 익은 토마토의 값 1부터 1을 더해줬기 때문에 -1





