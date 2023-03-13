import sys
# sys.stdin = open('in1.txt', 'rt') -> 채점
n, k = map(int, input().split())
# print(n, k) -> 8, 4

cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1 

    if cnt == k:
        print(i)
        break

else:
    print(-1)




