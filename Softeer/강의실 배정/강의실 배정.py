import sys
input = sys.stdin.readline
n = int(input()) # 강의 개수
time_lst = [list(map(int, input().split())) for _ in range(n)]

time_lst = sorted(time_lst, key=lambda x:(x[1], x[0]))
# print(time_lst)

cnt = 1

end = time_lst[0][1]
for i in range(1, n):
    if time_lst[i][0] >= end:
        cnt += 1
        end = time_lst[i][1]

print(cnt)