import sys
input = sys.stdin.readline

n = int(input())
ticketNum = list(map(int, input().split()))

ticketNum = sorted(ticketNum)

a = 1
for num in ticketNum:
    if num == a:
        a += 1
    else:
        continue

print(a)

