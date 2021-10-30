# 메모리: 44844KB, 시간: 4840ms
import sys
input = sys.stdin.readline

testCaseNum = int(input())
rotate = 0
while rotate < testCaseNum:
    applyNum = int(input())
    score_list =[]

    for i in range(applyNum):
        score1, score2 = map(int, input().split())
        score_list.append([score1,score2])

    score_list = sorted(score_list) # 서류 평가 순위로 고정

    first = score_list[0][1]
    cnt = 1 # 이미 첫번째 아이템에 있는 사람은 서류 평가 1등이므로 count를 해줌
    for i in range(1, len(score_list)):
        if first > score_list[i][1]: # 다음 사람이 면접 등수가 더 높으면 count해주고, 비교 기준인 first에 반환시켜줌
            cnt += 1
            first = score_list[i][1]

    print(cnt)
    rotate += 1










