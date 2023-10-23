import sys
from collections import deque

d = [[1,0],[0,1],[-1,0],[0,-1]]

def bfs(y,x):
    queue = deque()
    queue.append([y,x])
    visited[y][x] = True
    count = 1

    while queue:
        r,c = queue.popleft()
        
        for i in range(4):
            dr = r+d[i][0]
            dc = c+d[i][1]

            if(0<=dr<n and 0<=dc<n) and blockMap[dr][dc] ==1 and not visited[dr][dc]: 
                queue.append([dr,dc])
                visited[dr][dc] = True
                count+=1
    
    return count



n = int(sys.stdin.readline())

blockMap = [list(map(int, input())) for _ in range(n)]

visited = [[False]*(n) for _ in range(n)]


result = []
for i in range(n):
    for j in range(n):
        if blockMap[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i,j))

print(len(result))
result.sort()
for i in result:
    print(i)