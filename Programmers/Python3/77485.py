# 행렬 테두리 회전하기
def solution(rows, cols, queries):
    # 맵 만들기
    maps = [[0 for _ in range(cols)] for _ in range(rows)]
    num = 1
    for row in range(rows):
        for col in range(cols):
            maps[row][col] = num
            num += 1

    answer = []
    for x1, y1, x2, y2 in queries:
        start = maps[x1-1][y1-1] # 시작 지점 다음 위치에 처음 값이 들어오기 위해
        temp = start # 시작 기준 윗 값 반환

        # 왼쪽 세로
        for k in range(x1-1, x2-1):
            test = maps[k+1][y1-1] # 시작 값 저장
            maps[k][y1-1] = test # temp 위치에 아래 값 저장 -> 회전
            temp = min(temp, test) # 최소값 return

        # 하단 가로
        for k in range(y1 - 1, y2 - 1):
            test = maps[x2-1][k+1]
            maps[x2-1][k] = test
            temp = min(temp, test)

        # 우측 세로
        for k in range(x2-1, x1-1, -1):
            test = maps[k-1][y2-1]
            maps[k][y2-1] = test
            temp = min(temp, test)

        # 상단 가로
        for k in range(y2-1, y1-1, -1):
            test = maps[x1-1][k-1]
            maps[x1-1][k] = test
            temp = min(temp, test)

        maps[x1-1][y1] = start # 시작 값 반환
        answer.append(temp)

    return answer

# 클린코드 stack 활용 참고
# def solution(rows, columns, queries):
#     answer = []
#
#     board = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]
#     # print(board)
#
#     for a,b,c,d in queries:
#         stack = []
#         r1, c1, r2, c2 = a-1, b-1, c-1, d-1
#
#
#         for i in range(c1, c2+1):
#
#             stack.append(board[r1][i])
#             if len(stack) == 1:
#                 continue
#             else:
#                 board[r1][i] = stack[-2]
#
#
#         for j in range(r1+1, r2+1):
#             stack.append(board[j][i])
#             board[j][i] = stack[-2]
#
#         for k in range(c2-1, c1-1, -1):
#             stack.append(board[j][k])
#             board[j][k] = stack[-2]
#
#         for l in range(r2-1, r1-1, -1):
#             stack.append(board[l][k])
#             board[l][k] = stack[-2]
#
#         answer.append(min(stack))
#
#
#     return answer
