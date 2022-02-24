import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())
q = deque()
cnt = 1 # 최소값에서 1 더한 값 출력으로 초기화
answer = -1 # 만들수 없는 경우 초기화
q.append([a, b, cnt])
while q:
    a, b, cnt = q.popleft()
    if a == b:
        answer = cnt
        break

    if a * 2 <= b: # a의 연산을 했을 때 b보다 커진 값을 큐에 추가한 것은 의미가 없음 -> 처음에 크기 제한을 안걸고 했다 메모리 초과
        q.append([a * 2, b, cnt + 1])

    if (a * 10) + 1 <= b: # 위와 마찬가지
        q.append([(a * 10) + 1, b, cnt + 1])

print(answer)

