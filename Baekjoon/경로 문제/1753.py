import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

graph = defaultdict(list)
INF = int(1e9)
distance = [INF] * (V+1)

for _ in range(E):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        # 연결되있는 노드 가져오기
        for node in graph[now]:
            cost = dist + node[1]

            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(queue, (cost, node[0]))


dijkstra(start)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])