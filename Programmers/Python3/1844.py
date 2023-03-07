# 게임 맵 최단거리
from collections import deque
def solution(maps):
        # 방문 맵
        visited = [[0] * len(maps[0]) for i in range(len(maps))]

        # 방향(남, 북, 서, 동)
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        q = deque()
        q.append([0, 0, 1]); visited[0][0] = 1 # 시작위치, 길이 1 및 방문처리
        while q:
                y, x, dist = q.popleft()
                # 도착 지점에 왔을 때 거리 반환
                if x == len(maps[0]) - 1 and y == len(maps) - 1:
                        return dist

                for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        # 맵을 벗어나지 않으면서
                        if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                                # 벽이 아니면서 방문하지 않은 지점일 때
                                if maps[ny][nx] == 1 and not visited[ny][nx]:
                                        q.append([ny, nx, dist + 1]) # 현재 지점 저장 및 길이 저장
                                        visited[ny][nx] = 1 # 방문 처리

        return -1