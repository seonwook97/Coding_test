# n = 4
def solution(n):
    arr = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    a = 1

    for i in range(n):
        for j in range(i, n): # 아래로 이동
            if i % 3 == 0:
                x += 1

            elif i % 3 == 1: # 옆으로 이동
                y += 1

            elif i % 3 == 2: # 위로 이동
                x -= 1
                y -= 1

            arr[x][y] = a
            a += 1

    for item in arr:
        for i in item:
            if i != 0:
                answer.append(i)

    return answer
# print(answer)













