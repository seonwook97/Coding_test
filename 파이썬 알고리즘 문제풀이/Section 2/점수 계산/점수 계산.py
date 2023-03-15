import sys
# sys.stdin = open('in1.txt', 'rt')

n = int(input())
scores = list(map(int, input().split()))
result = 0 # 합산
cnt = 0 # 가산점
for score in scores:
    if score == 1:
        cnt += 1
        result += cnt # 가산점이 더해진 점수

    else:
        cnt = 0 # 연속이 끊기면 다시 가산점 초기화

print(result)


