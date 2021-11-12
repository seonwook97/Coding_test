import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 보드 크기
k = int(input()) # 사과 개수
apple = [list(map(int, input().split())) for i in range(k)] # 사과의 위치를 list로 담음

turnNum = int(input()) # 뱀의 방향 변환 횟수
num, turnInfo = 0, [list(input().split()) for i in range(turnNum)] # 뱀의 게임 시작으로부터 경과 시간, 방향 변환 정보
for info in turnInfo:
    info[0] = int(info[0]) # 게임 시작으로부터 경과 시간은 정수이므로 형변환

t = 0  # 시간
direction = 0 # 동, 서, 남, 북 이동 방향 초기화
snake = deque()

snake.append([1, 1]) # 뱀의 출발 지점
head = [1, 1] # 뱀의 머리 처음 지점

while True:
    t += 1 # 1초 경과할 때마다 뱀이 움직이는 경우들을 보여주자

    # 동, 서, 남, 북 이동
    if direction == 0: # 동
        head[1] += 1  # head의 열값을 1만큼 이동했으므로 동쪽

    elif direction == 1: # 남
        head[0] += 1 # head의 행값을 1만큼 이동했으므로 남쪽

    elif direction == 2: # 서
        head[1] -= 1 # head의 열값을 -1만큼 이동했으므로 서쪽

    else:
        head[0] -= 1 # head의 행값을 -1만큼 이동했으므로 북쪽

    # 보드 바깥에 부딪혔을 때
    if head in snake: # 자기 자신의 몸과 부딪혔을 경우
        print(t)
        break

    elif head[0] > n or head[0] < 1 or head[1] > n or head[1] < 1:
        print(t)
        break

    # 사과
    if head not in apple:  # 사과를 발견하지 못했을 때
        snake.popleft() # 뱀의 몸 길이를 줄여 꼬리의 위치값을 제거한다

    else:  # 발견했을 경우
        apple.remove(head) # 사과를 발견하면 뱀의 머리 위치와 사과의 위치가 같으므로 사과 위치 값을 제거

    # 머리 위치를 새로 저장
    snake.append([head[0], head[1]])

    # 방향 전환
    if num < turnNum and t == turnInfo[num][0]:
        if turnInfo[num][1] == 'D': # 오른쪽으로 90도 회전일 경우
            direction = (direction + 1) % 4

        else: # 왼쪽으로 90도 회전일 경우
            direction = (direction - 1) % 4

        num += 1


