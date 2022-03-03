import sys
input = sys.stdin.readline

n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]
work.sort(key=lambda x: x[1], reverse=True)
spare_time = work[0][1]
for i in range(n):
    spare_time = min(work[i][1], spare_time) - work[i][0]
print(spare_time)

