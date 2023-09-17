def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        # idx를 n으로 나눈 몫, 나머지와 배열의 숫자와의 관계
        answer.append(max(i // n, i % n) + 1)  
    return answer