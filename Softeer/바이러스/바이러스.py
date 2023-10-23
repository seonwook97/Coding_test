import sys

k, p, n = map(int,sys.stdin.readline().split())

for i in range(n):
    # 모듈러 산술: https://sskl660.tistory.com/75
    # k = k % 1000000007
    # p = p % 1000000007 
    k = (k * p) % 1000000007

print(k)