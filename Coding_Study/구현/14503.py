import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]
visited[r][c] = True
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
turnCnt = 0 # 회전 수
cnt = 1 # 시작한 자리 청소
while True:
  d -= 1
  if d == -1:
    d = 3 # 북 -> 서 -> 남 -> 동
  nx = r + dx[d]
  ny = c + dy[d]
  # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 청소
  if not visited[nx][ny] and graph[nx][ny] == 0:
    visited[nx][ny] = True
    r, c = nx, ny
    cnt += 1
    turnCnt = 0 # 이동한 위치에서 다시 탐색하므로 방향 전환 횟수 초기화
    continue

  else: # 왼쪽 방향에 청소할 공간이 없으므로 한번 더 왼쪽으로 회전
    turnCnt += 1

  if turnCnt == 4: # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
    nx = r - dx[d]
    ny = c - dy[d]
    if graph[nx][ny] == 0:
      r, c = nx, ny # 바라보는 방향을 유지한 채로 후진
      turnCnt = 0 # 이동한 위치에서 다시 탐색하므로 방향 전환 횟수 초기화

    else: # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우 작동을 멈춤
      break

print(cnt)








