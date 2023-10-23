import sys
import heapq
from collections import defaultdict

def dijkstra(start):
    global graph
    queue = []
    heapq.heappush(queue, [0, start])
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        
        for node in graph[now]:
            cost = max(dist, node[1])
            
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(queue, [cost, node[0]])

if __name__ == '__main__':
    n, m = map(int, input().split()) # n: 체육관수, m: 길의수
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c]) # 양방향

    distance = [int(1e9)] * (n+1)   

    dijkstra(1)

    for i in range(distance[n] + 1, distance[n] * 2):
        if i % 2 == 0:
            continue
        flag = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                flag = False
                break

        if flag:
            print(i)
            break
