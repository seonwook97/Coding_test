import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
n = int(input())
info_list = [list(map(int, input().split())) for _ in range(n)]
# 회의의 수가 많으려면 끝나는 시각이 빠른 순서로 정렬 되어야 하고,
# 또한 회의 시작 시각과 끝나는 시각이 같을 수 있기 때문에
# 추가로 시작 시각이 빠른 순서로 정렬을 해주어야 함
info_list.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = info_list[0][1] # 끝나는 시간 비교 <-> 다음 회의 시작 시간
for i in range(1, n):
    if info_list[i][0] >= end:
        cnt += 1
        end = info_list[i][1]

print(cnt)
# end = time.time()
# print(f"{end - start:.5f} sec")