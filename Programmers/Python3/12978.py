import heapq
from collections import defaultdict

def solution(N, road, K):
    start = 1

    graph = defaultdict(list)
    INF = int(1e9)
    distance = [INF] * (N+1)

    for item in road:
        graph[item[0]].append((item[1], item[2]))
        graph[item[1]].append((item[0], item[2]))


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

    cnt = 0
    for i in range(1, N+1):
        if distance[i] <= K:
            cnt += 1

    return cnt
