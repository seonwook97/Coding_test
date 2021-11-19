# n = 7
def solution(n):
    usage = 0
    while n > 0:
        r = n % 2
        if r == 1: # 1만큼 이동할때는 무조건 점프를 해야함
            usage += 1

        n = n // 2

    return usage

# print(usage)

# ((0 * 1 + 1) * 2 + 1) * 2 + 1 -> 7을 2로 나누었을 때 몫 3 나머지 1, 다시 몫 3을 2로 나누었을 때 몫 1 나머지 1...
# 몫을 도달 거리까지 남은 거리라고 생각하면 된다
# +의 개수는 곧 점프한 횟수

# 미친 풀이 (단순하게 생각하는법도 필요하다고 느끼는)
def solution(n):
    return bin(n).count('1')

