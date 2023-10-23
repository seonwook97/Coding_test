import sys
input = sys.stdin.readline

# 격자크기: n, 방문지점개수: m
n, m = map(int, input().split())

# 맵
maps = [list(map(int, input().split())) for _ in range(n)]

# 방문해야 하는 지점
loc = []
for _ in range(m):
    x, y = map(int, input().split())
    loc.append([x-1, y-1])

# 방문확인
visited = [[0 for _ in range(n)] for _ in range(n)]

# 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 경로개수
cnt = 0

# 경로탐색: dfs
def dfs(now, destIdx):
    global cnt # 경로개수 count
    if now == loc[destIdx]: # 도착했다면
        if destIdx == m - 1: # 방문지점의 마지막에 있다면
            cnt += 1
            return
        else:
            destIdx += 1 # 다음 방문위치 저장
    x, y = now
    visited[x][y] = True # 방문 확인
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 맵 안에 있으며, 방문하지 않았으며, 방문할 수 있는
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and maps[x][y] == 0:
            dfs([nx, ny], destIdx)
    visited[x][y] = False # 방문 초기화
    return 

# 시작
dfs(loc[0], 1) # 처음 시작 위치, 도착해야 하는 첫번째 지점

# 결과
print(cnt)