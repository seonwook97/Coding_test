import sys
n,m = map(int, input().split())
count = 0
strings = {sys.stdin.readline() for i in range(n)}
for j in range(m):
    a = sys.stdin.readline()
    if a in strings:
        count += 1
print(count)
