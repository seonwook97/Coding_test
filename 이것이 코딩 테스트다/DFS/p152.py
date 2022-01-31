# 음료수 얼려 먹기 p.152
graph = []
n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input())))

answer = 0


def dfs(x, y):
    if x <= -1 or x >= n or y < 0 or y >= m:  # 범위 벗어나면 종료
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True


dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            answer += 1

print(answer)
