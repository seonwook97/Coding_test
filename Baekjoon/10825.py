# 메모리: 62280KB, 시간: 432ms
import sys
input = sys.stdin.readline

n = int(input())
score_list = []
for i in range(n):
    score = list(input().split())
    score_list.append([score[0], int(score[1]), int(score[2]), int(score[3])])

score_list = sorted(score_list, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for score in score_list:
    name = score[0]
    print(name)


