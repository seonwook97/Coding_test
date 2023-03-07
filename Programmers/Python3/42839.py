# 소수 찾기
from itertools import permutations

# numbers = '011'
def solution(numbers):
    answer = []
    nums = [n for n in numbers]
    per = []
    for i in range(1, len(numbers) + 1):
        per += set(permutations(nums, i))
    new_nums = set(int(('').join(p)) for p in per)

    for n in new_nums:
        if n < 2: # 2보다 작을 경우 소수가 아님
            continue
        check = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                check = False
                break

        if check:
            answer.append(n)

    return len(answer)