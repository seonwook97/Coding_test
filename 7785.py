import sys
input = sys.stdin.readline

n = int(input())
log = {}
work = []

for a in range(n):
    name, status = input().split()
    log[name] = status

for name in log:
    if log[name] == 'enter':
        work.append(name)
    else:
        continue

for name in sorted(work, reverse=True):
    print(name)


