# 메모리: 32056KB, 시간: 3396ms
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
num_deque = deque([i for i in range(1, n+1)])
answer_list = []

while num_deque: # 덱에 있는 모든 숫자가 제거될 때까지
    for i in range(k - 1): # 제거할 k번째 자리의 숫자가 0번째 인덱스에 올 때까지 왼쪽으로 밀어줌
        num_deque.append(num_deque.popleft())
    answer_list.append(num_deque.popleft()) # 숫자를 제거함과 동시에 요세푸스 순열로 반환하기 위해 list에 담아줌

# 출력
print('<', end='')
for i in range(len(answer_list)):
    if i < (len(answer_list) - 1):
        print(answer_list[i], end=', ')

    else:
        print(answer_list[i], end='')
print('>', end='')


# 문제의 설명이 부실하다..
# 1 2 3 4 5 6 7
#
# (3) 4 5 6 7 1 2
#
# (3 6) 7 1 2 4 5
#
# (3 6 2) 4 5 7 1
#
# (3 6 2 7) 1 4 5
#
# (3 6 2 7 5) 1 4
#
# 최종: (3 6 2 7 5 1 4)