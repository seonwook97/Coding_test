from pprint import pprint
import sys
input = sys.stdin.readline

# '#' 위치찾기
def findDirection(x, y):
    cnt = 0 # '#'이 주변에 하나인 경우에만 return하도록 예외 cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] == '#':
            direction = i
            cnt += 1
    return (direction if cnt == 1 else -1)
        
# 시작점 찾기
def findStart(matrix):
    for x in range(h):
        for y in range(w):
            if matrix[x][y] == '#': # 로봇이 지나간 자리
                direction = findDirection(x, y) # findDirection: 현재 x,y 좌우상하 어느쪽에 '#'이 있는지
                if direction != -1: # '#'이 여러개인 경우
                    return x, y, direction

# bfs
def navigate(x, y, direction):
    prevDir = newDir = direction
    matrix[x][y] = '.' # 방문처리
    while True:
        while newDir == prevDir: # 직진
            print('A', end='')
            for _ in range(2): # 전진 2칸
                x, y = x + dx[newDir], y + dy[newDir]
                matrix[x][y] = '.'
            
            prevDir = newDir
            newDir = findDirection(x, y)

        if newDir == -1: # 탐색 마지막
            return 

        if (newDir - prevDir) % 4 == 1:
            print('L', end='')

        if (newDir - prevDir) % 4 == 3:
            print('R', end='')
        
        prevDir = newDir


if __name__ == '__main__':
    # h:세로, w:가로
    h, w = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(h)]
    # pprint(matrix)

    # 로봇이 보고 있는 방향
    directionMark = ['^', '<', 'v', '>']

    # 북 서 남 동 
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # 탐색
    x, y, direction = findStart(matrix)
    print(x+1, y+1) # index이므로 하나씩 추가
    print(directionMark[direction])
    navigate(x, y, direction)