import sys
input = sys.stdin.readline

n, k = map(int, input().split())
colors = [[] for _ in range(k+1)]
for _ in range(n):
    point = list(map(int, input().split()))
    colors[point[2]].append(point[:2])

def dfs(color, minX, maxX, minY, maxY):
    global minVal
    if color == k + 1:
        minVal = min(minVal, (maxX-minX)*(maxY-minY))
        return minVal

    for point in colors[color]:
        x, y = point[0], point[1]
        left, right = min(minX, x), max(maxX, x)
        bottom, top = min(minY, y), max(maxY, y)
        if minVal > (right-left) * (top-bottom):
            dfs(color+1, left, right, bottom, top)

minVal = 2000 ** 2
dfs(1, 1000, -1000, 1000, -1000) # 초기화
print(minVal)