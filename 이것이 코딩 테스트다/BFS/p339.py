# 특정 거리의 도시 찾기 p339
from collections import deque

N, M, K, X = map(int, input().split()) # N: 도시의 개수, M: 도로의 개수, K: 거리 정보, X: 출발 도시의 번호
graph = [[] for _ in range(N+1)]


# 모든 도로 정보 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# print(graph)
# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (N+1)
distance[X] = 0 # 출발 도시까지의 거리는 0

# BFS 수행
q = deque([X])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)