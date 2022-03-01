import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

visited = [[False] * n for _ in range(n)]
dy = [-1, 1, 0, 0] # 상, 하, 좌, 우
dx = [0, 0, -1, 1]

cnt = 0 # 집 개수 초기화
def dfs(y, x):
    visited[y][x] = True
    global cnt
    if graph[y][x] == 1:
        cnt += 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if not visited[ny][nx] and graph[ny][nx] == 1:
                dfs(ny, nx)

    return cnt

cnt_list = []
for i in range(n):
    for j in range(n):
        # dfs함수 안에서 방문을 할때마다 False -> True가 되기 때문에 아직 방문하지 않았으면서 집이 있는 곳에 대한 예외조건을 통해 어떤 지점에서 방문을 시작했을 때, 인접한 집들에 대한 모든 count를 구해줌
        if not visited[i][j] and graph[i][j] == 1:
            # print(dfs(i, j))
            cnt_list.append(dfs(i, j)) # 출력 및 단지 수를 구하기 위해 list에 담아줌
        cnt = 0 # 다음 방문 시작 지점에서 부터 인접한 집들을 count하기 위해 초기화

print(len(cnt_list))
for cnt in sorted(cnt_list):
    print(cnt)

