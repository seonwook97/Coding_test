# 메모리: 45112KB, 시간: 824ms
# 풀이 1
# 재귀를 활용한 이진탐색 함수 생성 후 출력
import sys
input = sys.stdin.readline

n = int(input())
n_list = list((map(int, input().split())))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

def find_num(num, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if num == n_list[m]:
        return 1
    elif num > n_list[m]:
        return find_num(num, m + 1, end)
    else:
        return find_num(num, start, m - 1)

for searchNum in m_list:
    start = 0
    end = n - 1
    print(find_num(searchNum, start, end))

# 메모리: 45104KB, 시간: 904ms
# 풀이 2
# 직관적 이진탐색
input_num = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

input_num2 = int(input())
numbers2 = list(map(int, input().split()))

for num in numbers2:
    left, right = 0, len(numbers) - 1
    is_find = False

    while True:
        median = (left + right) // 2

        if num == numbers[median]:
            print(1)
            is_find = True
            break

        elif num > numbers[median]:
            left = median + 1

        elif num < numbers[median]:
            right = median - 1

        if left > right:
            break

    if not is_find:
        print(0)




