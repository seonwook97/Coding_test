# 예상 대진표
def solution(n, a, b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a + 1) // 2, (b + 1) // 2 # 홀수가 더 작으 쪽이므로 + 1 후 나눔
    return answer