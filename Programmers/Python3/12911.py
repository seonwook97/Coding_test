# 다음 큰 숫자
def solution(n):
    # 조건 1
    answer = n + 1
    while True: # 조건 1과 조건 2를 만족하는 최솟값 찾을 때 까지
        # 조건 2
        if bin(answer)[2:].count('1') == bin(n)[2:].count('1'):
            return answer

        else:
            answer += 1 # 다음 큰 자연수로 조건 2 탐색