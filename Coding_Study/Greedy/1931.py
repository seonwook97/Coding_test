import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
# 회의의 수가 많으려면 끝나는 시각이 빠른 순서로 정렬 되어야 하고,
# 또한 회의 시작 시각과 끝나는 시각이 같을 수 있기 때문에
# 추가로 시작 시각이 빠른 순서로 정렬을 해주어야 함
board = sorted(board, key=lambda x:(x[1], x[0]))
# print(board)

cnt = 1
# 회의를 가장 많이 할 수 있는 순서로 정렬이 끝난 상태이므로
# 0번째 인덱스의 끝나는 시각을 기준으로 반복문을 통해 다음 회의 시작 시간과 비교를 해주면서 회의 수 count
end = board[0][1]
for i in range(1, n):
    if board[i][0] >= end:
        cnt += 1
        # 현재 회의 종료 시각이 다음 회의 시작 시각보다 작거나 같으면 다음 회의 종료 시각으로 업데이트
        # 그 다음 회의 시작 시각과 비교를 위해
        end = board[i][1]

print(cnt)
