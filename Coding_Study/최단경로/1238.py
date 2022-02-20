import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)] # 주어지는 그래프 정보 담는 N개 길이의 리스트 (가는)
distance = [INF] * (n+1) # 거리 테이블용 (가는)
graph_r = [[] for _ in range(n+1)] # 주어지는 그래프 정보 담는 N개 길이의 리스트 (돌아오는)
distance_r = [INF] * (n+1) # 거리 테이블용 (돌아오는)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph_r[b].append(((a, c)))

# 다익스트라 알고리즘
def dijkstra(start, distance, graph):
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

dijkstra(x, distance, graph)
dijkstra(x, distance_r, graph_r)

max_time = 0
for i in range(1, n+1):
    max_time = max(max_time, distance[i] + distance_r[i]) # 오고 가는 합의 최대

print(max_time)