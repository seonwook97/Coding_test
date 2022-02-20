import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

def bfs(start, end, maps):
    queue = deque()
    queue.append(start)
    visited = set()
    while queue:
        x = queue.popleft()
        visited.add(x)
        next_row = maps[x]
        for i in range(len(next_row)):
            if next_row[i] == 1:
                if i == end:
                    return 1

                if i not in visited:
                    queue.append(i)
                    visited.add(i)

    return 0

answer = [[0 for _ in range(n)] for _ in range(n)]
for y in range(n):
    for x in range(n):
        answer[y][x] = bfs(y, x, maps)

for list in answer:
    s = ''
    for num in list:
        s = s + str(num) + ' '
    print(s)
