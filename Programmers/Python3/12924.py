# 완전탐색
def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
    return answer

# 점화식(시간복잡도 개선)

# a + (a+1) + (a+2) + ... + (a+k-1) = k(2a+k-1)/2 = n
# a <= n
# k < n
# a, k : 자연수
# a = n/k + (1-k)/2

# a가 자연수려면,
# (1) n/k도 자연수 -> k는 n의 약수여야함
# (2)(1-k)/2가 정수려면 k는 홀수여야함
# (3) k < n

def solution(n):
    temp_list = []
    for i in range(1, n+1, 2):
        if n % i == 0:
            temp_list.append(i)
    return len(temp_list)


