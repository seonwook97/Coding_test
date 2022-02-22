import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 문제 수, m: 정보 수
graph = [[] for _ in range(n+1)]
inform = [0] * (n+1) # 간선의 수 -> 먼저 푸는 것이 좋은 문제에 대한 정보 개수 -> 문제와 문제의 연결
heap = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # 정보를 그래프에 담아줌
    inform[b] += 1 # b문제보다 선행해서 풀어야 좋은 a문제 개수 추가

for i in range(1, n+1):
    if inform[i] == 0: # 선행해서 풀어야 좋은 문제가 없는 겨우
        heapq.heappush(heap, i) # 힙은 최소값부터 꺼내므로 문제조건에 부합하게 문제번호가 적은 순서로 뽑을 수 있음

visited = []
def bfs():
    global visited
    while heap:
        x = heapq.heappop(heap) # 선행문제가 없는 문제들을 먼저 풀어줌 -> 문제번호가 적은 순서로
        visited.append(x)
        for i in graph[x]: # 선행문제가 있는 문제들을 풀어줌
            inform[i] -= 1 # 문제를 풀었으므로 -1
            if inform[i] == 0:
                heapq.heappush(heap, i) # 선행문제가 없는 경우와 동일하므로 힙에 넣어서 while문 실행

bfs()

answer = ''
for num in visited:
    answer += str(num) + ' '

print(answer)

