import sys
# sys.stdin = open('in1.txt', 'rt')
n = int(input())

rewards = []
for i in range(n):
    result = list(map(int, input().split()))
    if result[0] == result[1] and result[1] == result[2]: # 같은 눈이 3개
        rewards.append(10000 + 1000 * result[0])
        continue
    
    if result[0] == result[1] or result[0] == result[2]:
        rewards.append(1000 + result[0] * 100)
    
    if result[1] == result[2]:
        rewards.append(1000 + result[1] * 100)
    
    else:
        rewards.append(max(result) * 100)

print(max(rewards))