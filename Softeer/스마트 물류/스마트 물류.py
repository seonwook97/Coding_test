import sys
input = sys.stdin.readline

n, k = map(int, input().split())
line = list(str(input()))

cnt = 0
for i in range(n):
    if line[i] == 'P':
        for j in range(i-k, i+k+1):
            if j >= 0 and j <= n-1 and line[j] == 'H':
                cnt += 1
                line[j] = 'D'
                break
                
print(cnt)