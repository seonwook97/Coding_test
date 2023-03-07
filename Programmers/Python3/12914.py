# 멀리 뛰기
# DP
# 아무 칸도 뛰지 않는 경우 = 1개 x
# 1칸만 뛰는 경우 = 1개 -> dp[0]
# 2칸만 뛰는 경우 = 1칸만 뛰는 경우 + 2칸 뛰는 경우 2개 -> dp[1]
# 3칸만 뛰는 경우 = 2칸만 뛰는 경우 (1칸만 뛰면 됨) + 1칸만 뛰는 경우 (2칸만 뛰면 됨)
              # = 1칸만 뛰는 경우 + 2칸만 뛰는 경우  -> dp[2] = dp[0] + dp[1]

def solution(n):
    if n < 2:
        return n

    dp = [0 for _ in range(n)]
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1] % 1234567

# 재귀
# 시간초과
# def solution(n):
#     return (solution(n-1) + solution(n-2) if n > 2 else n)
