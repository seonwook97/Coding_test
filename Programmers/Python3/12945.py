# 피보나치 수
# 반복문
def fib(n):
    curr, next = 0, 1
    for _ in range(n):
        # F(n) = F(n-1) + F(n-2)
        curr, next = next, curr + next
    return curr % 1234567

# # 재귀 함수
# 재귀를 사용하면 시간초과
# def fib2(n):
#     if n == 0: # F(0) = 0
#         return 0
#     elif n == 1 or n == 2: # F(1) = 1, F(2) = 1
#         return 1
#     else:
#         return (fib2(n-1) - fib2(n-2)) % 1234567

