# 상하좌우 p110
n = int(input())

# plan
plans = list(input().split())

x, y = 1, 1

# 방향 (L, R, U, D)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동
    x, y = nx, ny

print(x, y)

