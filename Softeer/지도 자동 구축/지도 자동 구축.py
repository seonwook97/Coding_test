import sys
input = sys.stdin.readline
n = int(input())
answer = (2**(n-1)+1 + 2**(n-1))**2
print(answer)