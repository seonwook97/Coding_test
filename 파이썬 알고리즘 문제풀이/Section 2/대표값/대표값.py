import sys
# sys.stdin = open('in1.txt', 'rt')
n = int(input())
scores = list(map(int, input().split()))
avg = round(sum(scores) / n)
min = 2147000000
for idx, x in enumerate(scores):
    tmp = abs(x - avg) # 편차
    if tmp < min:
        min = tmp 
        score = x
        num = idx + 1

    elif tmp == min: # 점수가 같을 경우
        if x > score: # 점수가 큰 학생을 저장 - 여려명일 경우는 index가 변하지 않음 -> 번호가 작은 학생을 반환
            score = x 
            num = idx + 1 

print(avg, num)


