import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

graph = [[] for _ in range(n+1)] # 주어지는 그래프 정보 담는 N개 길이의 리스트
visited = [False] * (n+1) # 방문처리 기록용
distance = [INF] * (n+1) # 거리 테이블용

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

s, e = map(int, input().split()) # 출발, 도착 노드

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for v, w in graph[now]:
            cost = d + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

dijkstra(s)
print(distance[e])