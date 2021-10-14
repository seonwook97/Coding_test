n, m = map(int, input().split())
count = 0
s = []
for i in range(n):
    a = input()
    s.append(a)

for j in range(m):
    b = input()
    if b in s:
        count += 1
print(count)