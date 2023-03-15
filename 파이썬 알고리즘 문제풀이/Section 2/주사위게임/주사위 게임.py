import sys
# sys.stdin = open('in1.txt', 'rt')
n = int(input())
max = 0
for i in range(n):
    result = list(map(int, input().split()))
    result.sort()
    if result[0] == result[1] and result[1] == result[2]: # 같은 눈이 3개
        rewards = 10000 + 1000 * result[0]
    
    elif result[0] == result[1] or result[0] == result[2]:
        rewards = 1000 + result[0] * 100
    
    elif result[1] == result[2]:
        rewards = 1000 + result[1] * 100
    
    else:
        rewards = result[2] * 100

    if rewards > max:
        max = rewards
print(max)