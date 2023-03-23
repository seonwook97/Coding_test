import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
def check_sudoku(board):
    # 각 행에 대한 유효성 검사
    for i in range(9):
        row = []
        for j in range(9):
            if board[i][j] in row:
                return 'NO'
            else:
                row.append(board[i][j])
    
    # 각 열에 대한 유효성 검사
    for i in range(9):
        col = []
        for j in range(9):
            if board[j][i] in col:
                return 'NO'
            else:
                col.append(board[j][i])
    
    # 각 3x3 박스에 대한 유효성 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = []
            for k in range(3):
                for l in range(3):
                    if board[i+k][j+l] in box:
                        return 'NO'
                    else:
                        box.append(board[i+k][j+l])
    
    # 모든 검사를 통과하면 유효한 스도쿠
    return 'YES'

sudoku_map = [list(map(int, input().split())) for _ in range(9)]
print(check_sudoku(sudoku_map))

# end = time.time()
# print(f"{end - start:.5f} sec")