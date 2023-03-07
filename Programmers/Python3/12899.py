# 124 나라의 숫자
def solution(n):
    answer = ''
    list = ['1', '2', '4']

    while n > 0:
        n = n - 1
        answer = list[n % 3] + answer
        n = n // 3

    return answer