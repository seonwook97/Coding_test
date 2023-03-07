# 하샤드 수
def solution(x):
    list_num = list(str(x))
    sum_num = 0

    for i in range(len(list_num)):
        sum_num += int(list_num[i])

        if x % sum_num == 0:
            answer = True
        else:
            answer = False

    return answer




