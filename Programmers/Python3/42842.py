# def solution(brown, yellow):
#     total_cnt = brown + yellow # 가로 * 세로 = total_cnt
#     for b in range(1, total_cnt+1): # 세로가 가로보다 작거나 같으므로 세로를 기준으로 늘려가면서 조건 충족
#         if (total_cnt / b) % 1 == 0: # 자연수 조건: a * b = total
#             a = total_cnt / b
#             if a >= b: # a >= b 가로 >= 세로
#                 if brown == 2 * (a+b) - 4: # 갈색 타일 개수 조건
#                     answer = [a, b]
# 
#     return answer

# 직관적
def solution(brown, yellow):
    n = (brown - 4) // 2 # 직사각형의 4개 모서리 제외 후 반으로 나눈 값은 노란 타일의 가로 + 세로
    for i in range(n):
        x, y = i, n-i # y: 가로, x: 세로 가로의 길이가 세로보다 크거나 같음
        if x*y == yellow: # 가로 * 세로 = 개수
            return [y+2, x+2]