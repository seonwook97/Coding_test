import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터 수
c = int(input()) # 간선의 수
graph = [[] for _ in range(n+1)]
for _ in range(c):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]
cnt = 0
def dfs(start):
    global cnt
    visited[start] = True
    # print(x, end=' ')
    for node in graph[start]:
        if visited[node] == False:
            cnt += 1
            dfs(node)

dfs(1)
print(cnt)