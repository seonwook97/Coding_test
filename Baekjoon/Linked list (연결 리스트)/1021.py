# 메모리: 32056KB, 시간: 104ms
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
numToPick = list(map(int, input().split()))
num_dq = deque([i for i in range(1, n+1)])
operNum = 0

for num in numToPick:
    while True:
        if num_dq[0] == num: # 덱의 첫번째 인덱스가 뽑는 수와 같으면 덱에서 수를 뽑아내고 반복 종료
            num_dq.popleft()
            break

        else:
            if num_dq.index(num) < len(num_dq) / 2: # 뽑는 수의 인덱스가 덱의 길이의 반보다 작을 때
                while num_dq[0] != num:
                    num_dq.append(num_dq.popleft()) # 왼쪽으로 움직여야 연산의 합이 최소가 됨
                    operNum += 1

            else: # 뽑는 수의 인덱스가 덱의 길이의 반보다 크거나 같을 때
                while num_dq[0] != num:
                    num_dq.appendleft(num_dq.pop()) # 오른쪽으로 움직여야 연산의 합이 최소가 됨
                    operNum += 1

print(operNum)









