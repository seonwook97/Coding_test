import sys
# sys.stdin = open('in2.txt', 'rt')
n = int(input())

def count_primes(n):
    num_list = [True] * (n + 1)
    num_list[0], num_list[1] = False, False

    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(n ** 0.5) + 1):
        if num_list[i]:
            for j in range(i * i, n + 1, i):
                num_list[j] = False

    cnt = 0
    for num in num_list:
        if num:
            cnt += 1
    
    return cnt

print(count_primes(n))
