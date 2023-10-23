import sys
import bisect 
input = sys.stdin.readline 
# n = 자동차 개수, q = 줄 개수, 
n, q = map(int, input().split())
# n_lst = 연비 목록
n_lst = sorted(list(map(int, input().split())))
for _ in range(q):
    med = int(input()) # 중앙값
    idx = bisect.bisect_left(n_lst, med) # list안에 값이 없으면 list의 길이를 반환
    if idx != n and med == n_lst[idx]:
        print(idx * (n-idx-1))
    else:
        print(0)