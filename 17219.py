import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
for a in range(n):
    address, pw = input().split()
    dic[address] = pw

for a in range(m):
    print(dic[input().rstrip()])